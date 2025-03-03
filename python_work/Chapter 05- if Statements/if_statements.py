""" 5-1
cars = ["subaru", "volvo", "rav4", "nissan", "mercedes"]

cars_requested = ["subaru", "honda", "volvo"]

for car in cars:
  if car == "subaru":
    print(f"Your car is a {car.title()}")
  else:
    print(f"Your car is not a {car.title()}")

print(cars[0] == "subaru")
print(cars[1] == "subaru")
print(cars[2] == "subaru")
print(cars[3] == "subaru")
print(cars[4] == "subaru")"""


"""5-2
cars = ["subaru", "volvo", "rav4", "nissan", "mercedes"]
cars_requested = ["subaru", "honda", "volvo"]


for car in cars_requested:
  if car in cars:
    print(f"We've got a {car.title()}")
  else: print(f"We don't have a {car.title()}")"""

""" 5-3
alien_color = ["green", "yellow", "red"]

if "green" in alien_color:"""

"""5-4
alien_color = ["green", "yellow", "red"]

if "green" in alien_color:
  print("Player just earned 5 points")
if "yellow" in alien_color:
  print("Player just earned 10 points")
if "red" in alien_color:
  print("Player just earned 10 points")

for color in alien_color:
  if color == "green":
    print("player just won 5 points")
  else: print("Player just won 10 points")"""

"""5-5
alien_color = ["green", "yellow", "red"]

for color in alien_color:
  if color == "green":
    print("player just won 5 points")
  elif color == "yellow":
    print("Player just won 10 points")
  else: print("Player just won 10 points")"""


""" 5-6
age = 25

if age < 2:
  group = "baby"
elif age < 4:
  group = "toddler"
elif age < 13:
  group = "child"
elif age < 20:
  group = "teenager"
elif age < 65:
  group = "adult"
else: group = "elder"

print(f"This person in an {group}")

"""

""" 5-7
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
favorite_fruits = ["apple", "banana", "orange"]

for fruit  in favorite_fruits:
  if fruit in fruits:
    print(f"You must really enjoy {fruit.lower()}s!")
"""

""" 5-8 & 5-9
users = ["john", "paul", "richard", "admin", "george"]

## Map over the array of users
# for user in users:
#   if user == "admin":
#     print(f"Hello {user.title()}, would you like to see an status report?")
#   elif user == user:
#     print(f"Hello {user.title()}, thank you for logging in again")

if not users:
  print("We need some users")
else:
  for user in users:
    if user == "admin":
      print(f"Hello {user.title()}, would you like to see an status report?")
    elif user == user:
     print(f"Hello {user.title()}, thank you for logging in again")
"""

""" 5-10
current_users = ["JOHN", "paul", "richard", "admin", "george"]
new_users = ["john", "matthew", "GEORGE", "luke" , "saul"]

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
  if user.lower() in current_users_lower:
    print(f"{user.title()} is already taken, choose a new username.")
  else: print(f"{user.title()} isn't taken, this username is available.")"""


# 5-11
numbers = []

for number in range(1,10):
  numbers.append(number)

numbers_str = list(map(str, numbers))

for number in range(len(numbers_str)):
    position = numbers_str[number]
    if position == "1":
        numbers_str[number] += "st"
    elif position == "2":
        numbers_str[number] += "nd"
    elif position == "3":
        numbers_str[number] += "rd"
    else: numbers_str[number] += "th"

print(numbers_str)



