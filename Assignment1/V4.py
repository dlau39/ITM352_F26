# Interactive Quiz System, Fourth Version
# Make a dictionary with the questions and correct answers
# Allow the user to select from multiple choice answers
# Name: Dominic Lau
# Date: October 7, 2026

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
    "What is the capital of Canada?": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Brisbane"]
}

for question, answers in questions.items():
    correct_answer = answers[0]  # The first option is the correct answer
    sorted_answers = sorted(answers)  # Sort the answers alphabetically

    for label, answer in enumerate(sorted_answers, start=1):
        print(f"{label}. {answer}")

    answer_label = int(input(f"{question} "))
    answer = sorted_answers[answer_label - 1]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}.")