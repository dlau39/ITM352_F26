# Imports the HandyMath module to use its functions
import HandyMath

# Prompts the user to enter two numbers and stores them as floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calls the functions from the HandyMath module and prints the results
print(f"The midpoint is {HandyMath.midpoint(num1, num2)}")
print(f"The square root of {num1} is {HandyMath.squareroot(num1)}")
print(f"{num1} raised to the exponent {num2} is {HandyMath.exponent(num1, num2)}")
print(f"The maximum is {HandyMath.max(num1, num2)}")
print(f"The minimum is {HandyMath.min(num1, num2)}")