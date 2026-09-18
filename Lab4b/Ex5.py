# Ask the user for a sentence (using input()).
# Turn the sentence into a list of words (using split()).
# Reverse the list of words (using reverse()).
# Join the reversed list of words back into a string (using join()).
# Name: Dominic Lau
# Date: Sept. 18 2026

sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)
print("Reversed sentence: ", reversed_sentence)

joined_sentence = sentence + " " + reversed_sentence
print("Joined sentence: ", joined_sentence)