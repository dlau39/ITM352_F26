# Final version of Quiz Game
# Name: Dominic Lau
# Date: October 9, 2026

from string import ascii_lowercase
import random
import json
from pathlib import Path
import re

def choose_category(quizfiles):
    categories = [
        (
            re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", path.stem)
            .replace("_", " ")
            .replace("-", " ")
            .title(),
            path,
        )
        for path in quizfiles
    ]

    # This section of the code prints the available categories for the user to choose from.
    print("Available categories:")
    for number, (category, _) in enumerate(categories, start=1):
        print(f"{number}. {category}")

    # This section of the code handles the user's selection and returns the chosen quiz file path.
    while True:
        try:
            choice = int(input("Choose a category number: "))
        except ValueError:
            print("Please enter a number from the list.")
            continue

        # This makes sure that the user selects a valid category.
        if 1 <= choice <= len(categories):
            return categories[choice - 1][1]

        print(f"Please choose a number from 1 to {len(categories)}.")

quiz_files = sorted(
    Path(__file__).resolve().parent.glob("*.json"),
    key=lambda path: path.stem.casefold()
)

if not quiz_files:
    raise FileNotFoundError("No quiz category JSON files were found.")

quiz_file = choose_category(quiz_files)
try:
    with quiz_file.open("r", encoding="utf-8") as question_file:
        questions = json.load(question_file)
except json.JSONDecodeError as error:
    raise ValueError(f"{quiz_file.name} does not contain valid JSON.") from error

if not isinstance(questions, dict) or not questions:
    raise ValueError(
        f"{quiz_file.name} must contain a non-empty object of questions and answers."
    )

NUM_QUESTIONS_PER_QUIZ = 5
SCOREBOARD_FILE = Path(__file__).resolve().with_name("scoreboard.json")

def prepare_questions(questions, num_questions):
    num_question = min(num_questions, len(questions))
    return random.sample(list(questions.items()), num_question)


def load_scoreboard(scoreboard_file=SCOREBOARD_FILE):
    if not scoreboard_file.exists():
        return []

    try:
        scores = json.loads(scoreboard_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    if not isinstance(scores, list):
        return []

    return [
        {"name": entry.get("name", "Unknown"), "score": int(entry.get("score", 0))}
        for entry in scores
        if isinstance(entry, dict)
    ]


def save_scoreboard(scores, scoreboard_file=SCOREBOARD_FILE):
    scoreboard_file.write_text(json.dumps(scores, indent=2), encoding="utf-8")


def show_scoreboard(scores):
    print("\nTop scores:")
    ranked_scores = sorted(scores, key=lambda entry: entry["score"], reverse=True)[:10]

    if not ranked_scores:
        print("No scores recorded yet.")
        return

    for rank, entry in enumerate(ranked_scores, start=1):
        print(f"{rank}. {entry['name']} - {entry['score']}")


def record_score(name, score, scoreboard_file=SCOREBOARD_FILE):
    scoreboard = load_scoreboard(scoreboard_file)
    previous_high_score = max((entry["score"] for entry in scoreboard), default=0)

    scoreboard.append({"name": name, "score": score})
    ranked_scores = sorted(scoreboard, key=lambda entry: entry["score"], reverse=True)
    top_scores = ranked_scores[:10]
    save_scoreboard(top_scores, scoreboard_file)

    if score > previous_high_score:
        print(f"\nNew high score! {name} scored {score} points.")

    show_scoreboard(top_scores)


def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))  # Label answers with letters

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    return labeled_answers[answer_label]


def ask_question(question, alternatives):
    correct_answer = alternatives[0]  # The first option is the correct answer
    ordered_alternatives = random.sample(alternatives, len(alternatives))
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}.")
        return 0


questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)
num_correct = 0

# Main Loop
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

print(f"\nYou have answered {num_correct} out of {len(questions)} correctly.")

player_name = input("\nEnter your name for the scoreboard: ").strip() or "Player"
record_score(player_name, num_correct)