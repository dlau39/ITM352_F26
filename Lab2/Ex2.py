# Ask the user to enter their birth year. 
# Calculate their age based on the current year and print it out.
# Name: Dominic Lau
# Date: Sept. 2, 2026

birthYear = int(input('Enter your birth year: '))
currentYear = 2026
age = currentYear - birthYear

print(f'You entered {birthYear} as your birth year.')
print(f'You are {age} years old.')