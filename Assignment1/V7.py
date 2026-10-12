# Interactive Quiz System, Seventh Version
# Make a dictionary with the questions and correct answers
# Allow the user to select from multiple choice answers
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of the questions and answers
# Refactor the code to use functions.
# Name: Dominic Lau
# Date: October 9, 2026

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)
question_file.close()

NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions):
    num_question = min(num_questions, len(questions))
    return random.sample(list(questions.items()), num_question)

def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))  # Label answers with letters
          
    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
          
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")
          
    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]  # The first option is the correct answer
    ordered_alternatives = random.sample(alternatives, len(alternatives))  # Sort the answers alphabetically
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}.")
        return 0
        
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}.")
        return False


questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)
num_correct = 0

# Main Loop
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

print(f"\nYou have answered {num_correct} out of {len(questions)} correctly.")