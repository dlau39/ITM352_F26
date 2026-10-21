# Open names.txt and read its contents
# Append a new name at the end of the file

with open("names.txt", "r") as file_object: # Opens the file in read mode using with
    contents_list = file_object.readlines() # Read the contents of the file into a list
    print(contents_list) # Print the contents of the file

with open("names.txt", "a") as file_object: # Opens the file in append mode using with
    print("Appending a new name to the file...") # Print a message indicating that a new name is being appended
    file_object.write("Doe, John\n") # Append a new name to the end of the file