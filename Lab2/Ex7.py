# This program prompts the user to enter a number in Farenheit and then converts it to Celsius.
# Name: Dominic Lau
# Date: Sept. 4, 2026

fareinheitInput = input("Enter a temperature in Farenheit: ")
fareinheitFloat = float(fareinheitInput)
celsiusValue = (fareinheitFloat - 32) * 5/9

celsiusValueRounded = round(celsiusValue, 2)


print("You entered:", fareinheitFloat)
print("The temperature in Celsius is:", celsiusValueRounded)