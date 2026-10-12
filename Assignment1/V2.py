# Interactive Quiz System, Second Version
# Name: Dominic Lau
# Date: October 2, 2026

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the capital of Australia?", "Canberra")
]

for question, correct_answer in questions:
    answer = input(question + " ")
    if answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}', not {answer!r}.")