# This program prompts the user to enter a number in Farenheit and then converts it to Celsius.
# Create the conversion as a function
# Name: Dominic Lau
# Date: Sept. 4, 2026

def fareinheitToCelsius(fareinheit):
    celsius = (fareinheit - 32) * 5/9
    roundedCelsius = round(celsius, 2)
    return roundedCelsius

fareinheitInput = input("Enter a temperature in Farenheit: ")
fareinheitFloat = float(fareinheitInput)

celsiusValueRounded = fareinheitToCelsius(fareinheitFloat)

print("You entered:", fareinheitFloat)
print("The temperature in Celsius is:", celsiusValueRounded)