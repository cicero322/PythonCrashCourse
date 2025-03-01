""" 8.1
def display_sentence():
  print("In this chapter I'm learning about functions")
display_sentence()
"""
""" 8.2
def favorite_book(title):
  print(f"My favorite books is {title}")

favorite_book("1984")"""

""" 8.3
  def make_shirt(message,size):
  print(f"The shirt size is {size}, and on it is written: {message.title()}")

#Positional arguments
make_shirt("I'm paul muad'ib atreides","medium")

#Keyword arguments
make_shirt(message="I'm paul muad'ib atreides",size="medium")

#Keyword arguments
make_shirt(size= "medium",message="I'm paul muad'ib atreides")"""


""" 8.4
  def make_shirt(message="I love Python",size="large"):
  print(f"The shirt size is {size}, and on it is written: {message} ")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Capybara")"""

""" 8.5
def describe_city(city, country="Brazil"):
  print(f"{city.title()} is in {country.title()}.")

describe_city("São Paulo")
describe_city("Rio de Janeiro")
describe_city("Buenos Aires", "Argentina")
describe_city(country = "Argentina", city = "Buenos Aires")"""

""" 8.6
def city_country(city, country):
 return print(f"{city}, {country}")

city_1 = city_country("Paris","France")
city_2 = city_country("Oslo","Norway")
city_3 = city_country("Frankfurt","Germany")
"""

""" 8.7
  def make_album(artist,title,music=None):
  if music:
    person = {"name": artist, "album_title": title, "music":music }
    print(f"The album is by {artist}, titled {title} has {music} songs ")
  else:
    person = {"name": artist, "album_title": title}
    print(f"The album is by {artist}, titled {title}")
  return person

test = make_album("Paul McCartney","Ram")
print("\n")
test_2 = make_album("John Lennon","Imagine",10)

# Keyword arguments
# test_2 = make_album(artist="John Lennon",title="Imagine",music=10)
"""

""" 8.8
  def make_album(artist,title):
    person = {"name": artist, "album_title": title}
    print(f"\nThe album is titled {title.title()}, by {artist.title()}.")
    return person

while True:
  print("\nInsert 'q' at any time to quit")
  album_name = input("Insert the title of the album: ")
  if album_name.lower() == "q":
    break
  print("Insert 'q' at any time to quit")
  artist_name = input("Insert the name of the artist: ")
  if artist_name.lower() == "q":
    break
  make_album(title=album_name, artist=artist_name)
"""

""" 8.9
unsent_messages = ["Good Morning", "Are you up?", "Would you like to go to the theater?"]

def show_messages(unsent_messages):
  for received_message in unsent_messages:
    print(f"Received message: {received_message}")


show_messages(unsent_messages)

"""

""" 8.10
def sent_messages(unsent_messages, received_messages):
  while unsent_messages:
    current_messages = unsent_messages.pop(0)
    print(f" Sending message: {current_messages} ...")
    received_messages.append(current_messages)


def received_message(received_messages):
  for received_message in received_messages:
    print(f"Received message: {received_message}")

unsent_messages = ["Good Morning", "Are you up?", "Would you like to go to the theater?"]
received_messages = []

"""
""" 8-13
  def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Cicero', 'Alves',location='Brazil', field='physics', programming_language="python")
print(user_profile)"""



""" 8.11
  def sent_messages(unsent_messages, received_messages):
  while unsent_messages:
    current_messages = unsent_messages.pop(0)
    print(f" Sending message: {current_messages} ...")
    received_messages.append(current_messages)


def received_message(received_messages):
  for received_message in received_messages:
    print(f"Received message: {received_message}")

unsent_messages = ["Good Morning", "Are you up?", "Would you like to go to the theater?"]
received_messages = []

sent_messages(unsent_messages[:], received_messages)
received_message(received_messages)
"""

""" 

#Array test with len > 1
sandwiches = [
  "Grilled Cheese",
  "Chicken Parmesan",
  "Egg Salad Sandwich"
]

def call_sandwich(*sandwich):
 if len(sandwiches) > 1:
    print("\nWe have the following sandwiches:")
    for sandwich in sandwiches:
      print(f"- {sandwich}")
 else: 
    print(f"\nWe have the following sandwich:")
    for sandwich in sandwiches:
      print(f"- {sandwich}")


#Call function with len > 1
call_sandwich(sandwiches)


#Array test with len = 1
sandwiches = [
  "Grilled Cheese"
]

#Call function with len = 1
call_sandwich(sandwiches)


# def call_sandwich(*sandwiches):
#   if len(sandwiches) > 1:
#     print("\nWe have the following sandwiches:")
#     for sandwich in sandwiches:
#       print(f"- {sandwich}")
#   else: 
#     print(f"\nWe have the following sandwich:")
#     for sandwich in sandwiches:
#       print(f"- {sandwich}")


# # Test with arbitrary number of arguments, len >1
# call_sandwich("Grilled Cheese", "Chicken Parmesan","Egg Salad Sandwich")
# # Test with one argument, len = 1
# call_sandwich("Tuna")"""


""" 8.14
def call_car(manufacturer,input_year,**general_info):
    general_info['Manufacturer'] = manufacturer
    general_info['Built_in'] = input_year
    return general_info


car_info = call_car("Volvo","2025",country="Sweden", continent="Europe", model = "XC90")
print(car_info)"""


# 8.16
from printing_functions import * 


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


p.print_models(unprinted_designs, completed_models)
p.show_completed_models(completed_models)
