# First version of the quiz game
# Name: Dominic Lau
# Date: October 2, 2026

answer = input("What is the capital of France? ")
if answer == "Paris" or answer == "paris":
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is 'Paris', not {answer!r}.")

answer = input("What is the capital of Japan? ")
if answer == "Tokyo" or answer == "tokyo":
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is 'Tokyo', not {answer!r}.")