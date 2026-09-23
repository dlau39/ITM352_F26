# Name: Dominic Lau
# Date: Sept 23. 2026

trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = ["$6.25", "$5.25", "$10.50", "$8.05"]

trips = dict(zip(trip_durations, trip_fares))
print(trips)

trip_num = int(input("What trip do you want?"))

print("The duration of the trip is:", trip_durations[trip_num - 1], "miles")  # Accessing the trip duration based on user input
print("The fare of the trip is:", trip_fares[trip_num - 1])  # Accessing the trip fare based on user input