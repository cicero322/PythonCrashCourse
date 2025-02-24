"""  6-1

info = {'first_name': 'Roger', 'last_name': 'Penrose', 'age': '93',  'location': 'Oxford'}

print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['location'])
 """


""" 6-2
print("\nSome celebrities have their own favorite numbers: ")

celebrities_numbers = {"Michael Jackson": "7", "Barbara Streissand" : "24", "John Lennon" : "9", "Elvis Presley":  "7", "Beyoncé" :"4"}
for key, value in celebrities_numbers.items():
    print(f"{key.title()} : {value.title()}")  """

"""  6-3
functions_descriptions = {"print": "Is a function that logs a pre-define text", "array" : "Is a list of values", "len()" : "is a method that returns the lenght of an array", "for" : "starts a loop of repetition", "if": "do something when a conditional is met"}

print("\nprint: ")
print(functions_descriptions["print"])

print("\narray:")
print(functions_descriptions["array"])

print("\nlen():")
print(functions_descriptions["len()"])

print("\nfor:")
print(functions_descriptions["for"])

print("\nif:")
print(functions_descriptions["if"]) """

""" 6-4
functions_descriptions = {"print": "Is a function that logs a pre-define text", "array" : "Is a list of values", "len()" : "is a method that returns the lenght of an array", "for" : "starts a loop of repetition", "if": "do something when a conditional is met"}

for key, value in functions_descriptions.items():
    print(f"\n{key}: {value.capitalize()}") """

""" 6-5

rivers = {"nile" : "egypt" , "amazon" :"brazil", "mississipi": "USA"}

for key, value in rivers.items():
    print(f"The {key.title()} is a river located in {value.title()}")

for key ,value in rivers.items():
    print(f"{key.title()}")


for key ,value in rivers.items():
    print(f"{value.title()}")
 """

""" 6.6 
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

users = ["jen", "saul", "sarah", "phillip"]

for user in users:
    if user.lower() in (key.lower() for key in favorite_languages):
        print(f"Thank you taking our poll, {user.title()}")
    else: print(f"Would you like to take your poll, {user.title()}? ")
 """



"""  6.7

physicists_info = {
    'roger': {'last_name': 'penrose', 
    'age': '93',
    'location': 'Oxford',
    'country': "uk"
    },
    'brian': {"last_name" : "cox",
    "age": "56",
    "location":"london",
    "country": "uk"
    },
    'neil': {"last_name": "deGrasse Tyson",
    "age": "65",
    "location": "new york",
    "country": "usa"}

}

print("The following list consist of famous physicists:")
for key, values in physicists_info.items():
    print(f"\t{key.title()} {values["last_name"].title()}, is {values["age"]} and lives in {values["location"].title()}, {values["country"].upper()} ")
 """

""" 6.8 
animals_info = { 
    "larry" : {
    "species" : "cat",
    "location" : "Downing Street, UK",
    "fame_reason" : "Chief Mouser to the Cabinet Office",
    },
    "moo Deng" : {
    "species" : "pygmy hippopotamus",
    "location" : "Chonburi, Thailand.",
    "fame_reason" : "her playful personality",
    },
    "lin bing" : {
    "species" : "panda",
    "fame_reason" : "first giant panda born in Thailand",
    "location" : "Chiang Maia, Thailand"
    }

}

for key, values in animals_info.items():
    print(f"{key.title()} is a {values["species"].title()}, famous for {values["fame_reason"]}, currently in {values["location"]} ")
 """


""" 6-9
favorite_places = {
    "paris" : {
        "name": "pierre",
        "attractions" : "Eiffel Tower, Louvre Museum, Notre-Dame, Montmartre, Champs-Élysées",
        "country" : "france",
        "climate" : "oceanean",
    },
    "athens" : {
        "name": "constantine",
        "attractions" : "Acropolis & Parthenon, Ancient Agora, Plaka district.",
        "country" : "greece",
        "climate" : "mediterranean",
    },
    "barcelona" : {
        "name": "pedro",
        "attractions" : "Sagrada Familia, Park Güell, Gothic Quarter, La Rambla",
        "country" : "spain",
        "climate" : "mediterranean",
    },
}

for key,values in favorite_places.items():
    print(f"\n{values["name"].title()}'s favorite place is {key.title()}")"""



""" 6-11
    favorite_places = {
    "paris" : {
        "attractions" : "Eiffel Tower, Louvre Museum, Notre-Dame, Montmartre, Champs-Élysées",
        "country" : "france",
        "population" : "11.28 million",
        "climate" : "oceanean",
    },
    "athens" : {
        "attractions" : "Acropolis & Parthenon, Ancient Agora, Plaka district.",
        "country" : "greece",
        "population" : "3.16 million",
        "climate" : "mediterranean",
    },
    "barcelona" : {
        "attractions" : "Sagrada Familia, Park Güell, Gothic Quarter, La Rambla",
        "country" : "spain",
        "population" : "5.71 million",
        "climate" : "mediterranean",
    },
}

print("The following list ")
for key,values in favorite_places.items():
    print(f"\n{key.title()}'s metropolitan population is approximately {values["population"]}, it's climate is {values["climate"]}, located in {values["country"].title()}, among main atractions are: \n{values["attractions"]}") """



# 6.11 
print("\nSome celebrities have their own favorite numbers: ")

celebrities_numbers = {"Michael Jackson": ["7","2"], 
"Barbara Streissand" : ["24"], 
"John Lennon" : ["9"], 
"Elvis Presley":  ["7"], 
"Beyoncé" :["4"]
}
for key, value in celebrities_numbers.items():
    if len(value) > 1: 
        print(f"{key.title()} favorite numbers are:") 
    else: print(f"{key.title()} favorite number is: ")
    
    for number in value:
        print(f"{number.title()}")

