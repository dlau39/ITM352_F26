# Define a list of survey response values (5, 7, 3, 8) and store them
# in a variable. Define a tuple of response 10s (1012, 1035, 1021, and 1053).
# and add them to the list.
# Name: Dominic Lau
# Date: Sept. 16 2026

response_values = [5, 7, 3, 8]
response_values.sort()
response_ids = (1012, 1035, 1021, 1053)
response_values.append(response_ids)

print("Combined response values and IDs:", response_values)

response_values_new = [(1012,5), (1035,7), (1021,3), (1053,8)]
print("Combined response values and IDs as tuples:", response_values_new)