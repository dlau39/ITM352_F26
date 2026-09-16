# Try to append to a tuple. It won't work.
# Name: Dominic Lau
# Date: Sept. 16 2026

survey_respondents = (1012, 1035, 1021, 1053)
# survey_respondents.append(1054)  # This will raise an AttributeError

survey_respondents = survey_respondents + (1054,)  # This will work, creating a new tuple
print("Updated survey respondents:", survey_respondents)