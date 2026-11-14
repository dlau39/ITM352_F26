import json
import os
import random
import re
import secrets
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for


QUIZ_DIRECTORY = Path(__file__).resolve().parent
SCOREBOARD_FILE = QUIZ_DIRECTORY / "scoreboard.json"
NUM_QUESTIONS_PER_QUIZ = 5


def get_categories():
    categories = []
    for path in sorted(QUIZ_DIRECTORY.glob("*.json"), key=lambda item: item.stem.casefold()):
        if path.name == "scoreboard.json":
            continue
        name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", path.stem)
        name = name.replace("_", " ").replace("-", " ").title()
        categories.append({"name": name, "filename": path.name})
    return categories


def load_questions(filename):
    category_files = {category["filename"] for category in get_categories()}
    if filename not in category_files:
        return None

    path = QUIZ_DIRECTORY / filename
    try:
        questions = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Unable to read quiz category {filename}.") from error

    if not isinstance(questions, dict) or not questions:
        raise ValueError(f"{filename} must contain a non-empty object of questions and answers.")
    if any(
        not isinstance(question, str)
        or not isinstance(answers, list)
        or not answers
        or any(not isinstance(answer, str) for answer in answers)
        for question, answers in questions.items()
    ):
        raise ValueError(f"{filename} must map each question to a list of answer choices.")

    return questions


def load_scoreboard():
    if not SCOREBOARD_FILE.exists():
        return []

    try:
        scores = json.loads(SCOREBOARD_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    if not isinstance(scores, list):
        return []

    return [
        {"name": entry.get("name", "Unknown"), "score": int(entry.get("score", 0))}
        for entry in scores
        if isinstance(entry, dict)
    ]


def record_score(name, score):
    scoreboard = load_scoreboard()
    previous_high_score = max((entry["score"] for entry in scoreboard), default=0)
    scoreboard.append({"name": name, "score": score})
    scoreboard.sort(key=lambda entry: entry["score"], reverse=True)
    scoreboard = scoreboard[:10]
    SCOREBOARD_FILE.write_text(json.dumps(scoreboard, indent=2), encoding="utf-8")
    return scoreboard, score > previous_high_score


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)


def render_current_question(error=None, status=200):
    quiz = session.get("quiz")
    if not quiz:
        return redirect(url_for("index"))

    question_number = quiz["question_number"]
    if question_number >= len(quiz["questions"]):
        return redirect(url_for("result"))

    question = quiz["questions"][question_number]
    return (
        render_template(
            "quiz.html",
            question=question["question"],
            options=question["options"],
            question_number=question_number + 1,
            total_questions=len(quiz["questions"]),
            error=error,
        ),
        status,
    )


@app.route("/", methods=["GET", "POST"])
def index():
    categories = get_categories()
    error = None

    if request.method == "POST":
        filename = request.form.get("category", "")
        try:
            category_questions = load_questions(filename)
        except ValueError as exception:
            error = str(exception)
        else:
            if category_questions is None:
                error = "Please select a valid quiz category."
            else:
                sampled_questions = random.sample(
                    list(category_questions.items()),
                    min(NUM_QUESTIONS_PER_QUIZ, len(category_questions)),
                )
                quiz_questions = []
                for question, answers in sampled_questions:
                    quiz_questions.append(
                        {
                            "question": question,
                            "correct_answer": answers[0],
                            "options": random.sample(answers, len(answers)),
                        }
                    )

                player_name = request.form.get("name", "").strip()[:40] or "Player"
                session.clear()
                session["quiz"] = {
                    "name": player_name,
                    "questions": quiz_questions,
                    "question_number": 0,
                    "score": 0,
                }
                return redirect(url_for("quiz"))

    return render_template(
        "index.html",
        categories=categories,
        scoreboard=load_scoreboard()[:10],
        error=error,
    ), (400 if error else 200)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz_state = session.get("quiz")
    if not quiz_state:
        return redirect(url_for("index"))

    if request.method == "POST":
        current_question = quiz_state["questions"][quiz_state["question_number"]]
        answer = request.form.get("answer")
        if answer not in current_question["options"]:
            return render_current_question("Select one of the answer choices.", 400)

        if answer == current_question["correct_answer"]:
            quiz_state["score"] += 1
        quiz_state["question_number"] += 1
        session["quiz"] = quiz_state

        if quiz_state["question_number"] == len(quiz_state["questions"]):
            scoreboard, is_high_score = record_score(quiz_state["name"], quiz_state["score"])
            session["result"] = {
                "name": quiz_state["name"],
                "score": quiz_state["score"],
                "total_questions": len(quiz_state["questions"]),
                "is_high_score": is_high_score,
                "scoreboard": scoreboard,
            }
            return redirect(url_for("result"))

    return render_current_question()


@app.route("/result")
def result():
    result_data = session.get("result")
    if not result_data:
        return redirect(url_for("index"))
    return render_template("results.html", **result_data)


if __name__ == "__main__":
    app.run(debug=True)
