'''
Create a function—call it squareroot—that takes a number and returns the square root of that number. Use the fact that the square root of n is n**0.5.
'''
num = int(input("Enter a number to find its square root: "))

def squareroot(num):
    return num**0.5

print(squareroot(num))