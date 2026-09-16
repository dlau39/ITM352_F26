# Name: Dominic Lau
# Date: Sept. 16 2026

first = input("Enter the first name: ")
middle = input("Enter the middle initial: ")
last = input("Enter the last name: ")

full_name = first + " " + middle + ". " + last
print("Full name:", full_name)

print(f"Your full name using the f-string is: {first} {middle}. {last}")
print("Your full name using "+ "%" +" formatting is: %s %s. %s" % (first, middle, last))
print("Your full name using format method is: {} {}. {}".format(first, middle, last))
print("Your full name using list joins is: " + " ".join([first, middle + ".", last]))
