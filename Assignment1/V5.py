# Interactive Quiz System, Fifth Version
# Make a dictionary with the questions and correct answers
# Allow the user to select from multiple choice answers
# Improve the look and usability. Keep track of correct answers.
# Name: Dominic Lau
# Date: October 7, 2026

from string import ascii_lowercase

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
    "What is the capital of Canada?": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Brisbane"]
}

num_correct = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correct_answer = answers[0]  # The first option is the correct answer
    print(f"\nQuestion {num}: {question}")
    sorted_answers = sorted(answers)  # Sort the answers alphabetically
    labeled_answers = dict(zip(ascii_lowercase, sorted_answers))  # Label answers with letters

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    answer_label = input("Choice? ").lower()
    answer = labeled_answers.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}.")
    
print(f"\nYou have answered {num_correct} out of {len(questions)} correctly.")