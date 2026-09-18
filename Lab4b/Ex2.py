# Properly format an inputted name in title case
# Name: Dominic Lau
# Date: Sept. 18 2026

raw_name = input("Enter your name: ")

stripped_name = raw_name.strip(" d")
title_case_name = stripped_name.title()
print("Formatted name in title case: ", title_case_name)

