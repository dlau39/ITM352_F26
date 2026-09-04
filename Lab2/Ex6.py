# This program converts weight from pounds to kilograms and displays the result.
# Name: Dominic Lau
# Date: Sept. 4, 2026

# print("The weight in kilograms is:", float(input("Enter weight in pounds: "))*0.453592)

KG_TO_LBS = 0.453592
weightInPounds = input("Enter weight in pounds: ")
weightInPoundsFloat = float(weightInPounds)
weightInKilograms = weightInPoundsFloat * KG_TO_LBS

print("You entered:", weightInPoundsFloat)
print("The weight in kilograms is:", weightInKilograms)