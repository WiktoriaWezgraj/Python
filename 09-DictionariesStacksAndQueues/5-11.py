'''Write a program to record voting. Voting results are saved in the voting.json file with the structure below. 
The program takes a person's name from the keyboard and increases the number of votes for that person by 1. 
If this is a new person, they are added to the list with a vote count of 1. 
You can run the program multiple times to add additional votes to the json file.

{
   person_name: number of votes,
   person_name: number of votes,
   ...
   ...
}'''

import json

try:
    # Read the contents of the JSON file
    with open('voting.json', 'r') as file:
        content = json.load(file)
except FileNotFoundError:
    # Initialize an empty dictionary if the file doesn't exist
    content = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ').strip()

# Update the vote count
if person_name in content:
    content[person_name] += 1
else:
    content[person_name] = 1

# Save updated voting data to the JSON file
with open('voting.json', 'w') as file2:
    json.dump(content, file2, indent=4)  # Save with indentation for readability

print(f"Vote recorded for {person_name}.")

