# Save the dictionary of quiz questions to a JSON file
import json

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Japan?": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
    "What is the capital of Canada?": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
    "What is the capital of Italy?": ["Rome", "Milan", "Naples", "Venice"]
}

filename = "quiz_questions.json"

# Open the file in write mode and save the dictionary as JSON
with open(filename, 'w') as file:
    json.dump(questions, file, indent=2)

print(f"Quiz questions have been saved to {filename}.")