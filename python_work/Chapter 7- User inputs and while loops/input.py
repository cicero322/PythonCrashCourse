""" 7.1 
car = input("Insert the car that you'd like: ")

print(f"Let me check if I can find you an {car.title()}")
 """

""" 7.2 
seats = input("Insert how many guests you have: ")

if int(seats) > 8:
    print("You'll have to wait for a table")
else: print("Your table is ready") """

""" 7.3
number = input("Insert your number: ")

if int(number) % 10 == 0:
    print("The given number is a multiple of 10")
else:print("The given number isn't a multiple of 10")
 """

""" 7.4
toppings = ""

while toppings != "quit":
    print("Type 'quit' at any time to quit")
    toppings = input("Insert the topping that you'd like: ")
    if toppings != "quit":
        print(f"We are adding {toppings} to your pizza ...")

print({toppings}) """

""" 7.5
age = input("Insert the user age: ")

if int(age) < 3 :
    cost = 0 
elif int(age) < 12:
    cost = 10
else: cost = 15

print(f"Your age is {age}, the cost of the ticket is ${cost}")
 """


""" 7.6

toppings = ""


# while toppings != 'quit':
#    print("Enter 'quit' anytime to stop the program")
#    toppings = input(f"What topping would you like: ")
#    if toppings != 'quit':
#       print(toppings)

# active = True

# while active:
#   print("Enter 'quit' anytime to stop the program")
#   toppings = input(f"What topping would you like: ")

#   if toppings == "quit":
#     active = False
#   else: print(f"{toppings}")


# active = True

# while active:
#   print("Enter 'quit' anytime to stop the program")
#   toppings = input("What topping would you like: ")


#   if toppings == "quit":
#     break
#   else: print(f"{toppings}")

current_number = 0


even = []

while current_number < 10:
  current_number += 1
  if current_number % 2 == 1:
    continue
  else: even.append(current_number)

print(even)"""

""" 7.7 # This is an deliberate infinite loop
i = 0

while i < 10:
    print(i)
 """

""" 7-8
sandwich_orders = ["grilled cheese","chicken caesar","tuna salad", "veggie sandwich"]
finished_sandwiches = []

while sandwich_orders:
  current_order = sandwich_orders.pop()
  print(f"Making {current_order.title()}...")
  finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
  print(f"{finished_sandwich.title()}")
"""

""" 7.9
sandwich_orders = ["grilled cheese","pastrami","chicken caesar","pastrami", "tuna salad", "veggie sandwich", "pastrami"]
finished_sandwiches = []

print("We are out of pastrami, Thank you for your cooperation.")
while "pastrami" in sandwich_orders:
  sandwich_orders.remove("pastrami")

while sandwich_orders:
  current_order = sandwich_orders.pop()
  print(f"Making {current_order.title()}...")
  finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
  print(f"{finished_sandwich.title()}")
"""


#7-10
response = {}

polling = True

while polling:
  name = input("What is your name?: ")
  location = input("What is your dream location?: ")

  response[name] = location

  continue_polling = input("Would you like another person to answer?: ")
  
  if continue_polling.lower() == "no":
    polling = False

print("\n--- Polling results: ---")
for key, values in response.items():
      print(f"{key.title()}'s dream location is {values.title()}")