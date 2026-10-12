# Interactive Quiz System, Third Version
# Make a dictionary with the questions and correct answers
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
    for answer in answers:
        print(f"- {answer}")
    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}', not {answer!r}.")