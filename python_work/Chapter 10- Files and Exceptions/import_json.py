""" 10-11 & 10-12
from pathlib import Path
import json

path = Path("favorite_number.json")

contents = path.read_text()

if contents:
    print(f"I know your favorite number! It's {json.loads(contents)}.")
else:
    input_number = input("What is your favorite number? ")
    json.dumps(input_number)
    path.write_text(input_number)
    print("Your favorite number has been saved.") """


# 10-12 & 10-13

from pathlib import Path
import json

path = Path("user_data.json")

# Check if the file exists and has content; otherwise, initialize an empty dictionary
contents = path.read_text()

if contents:
    user_values = json.loads(contents)
else:
    user_values = {}


username = input("What is your username?: ")

if username in user_values:
    print("User found:")
    for key, value in user_values[username].items():
        print(f"{key} : {value}")
else:
    print("No user data found.")
    user_data = {}
    user_data["name"] = input("What is your name? ")
    user_data["favorite_country"] = input("What is your favorite country? ")
    
    # Update the user_values dictionary with the new user data
    user_values[username] = user_data
    
    # Write the updated dictionary back to the file
    path.write_text(json.dumps(user_values))
    print("Your data has been saved.")
