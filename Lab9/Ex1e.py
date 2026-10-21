# Read the entire file using readlines()

with open("names.txt", "r") as file_object: # Opens the file in read mode using with
    names = file_object.readlines() # Read all lines of the file into a list
    print(f"Number of names in the file: {len(names)}") # Print the number of names in the file
    for name in names:
        print(name.strip()) # Print each name without the newline character