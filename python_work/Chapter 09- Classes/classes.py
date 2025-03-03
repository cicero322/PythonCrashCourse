""" 9.1
class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, a {self.cuisine_type.title()} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open")


my_restaurant = Restaurant("Omelette du Fromage", "French")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

"""
"""
class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, a {self.cuisine_type.title()} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open")

# Define Restaurant
my_restaurant = Restaurant("Omelette du Fromage", "French")
# Invokes Restaurant
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Define Restaurant
thai_restaurant = Restaurant("Golden Wok", "Thai")
# Invokes Restaurant
thai_restaurant.describe_restaurant()
thai_restaurant.open_restaurant()

# Define Restaurant
portuguese_restaurant = Restaurant("Casa do Pasto","portuguese")
# Invokes Restaurant
portuguese_restaurant.describe_restaurant()
portuguese_restaurant.open_restaurant()"""

""" 9.3
    class User:

    def __init__(self,first_name,last_name,age, country):
        self.first_name = first_name
        self.last_name = last_name  
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, originally from {self.country}, was {self.age} at time of death")

    def greet_user(self):
        print(f"Greetings, {self.first_name}.\n")

def user_1():
    localData = User("Albert","Einstein","76","Germany")
    localData.describe_user()
    localData.greet_user()

user_1()


def user_2():
    localData = User("Maria","Curie","66","France")
    localData.describe_user()
    localData.greet_user()

user_2()

def user_3():
    localData = User("Isaac","Newton","84","England")
    localData.describe_user()
    localData.greet_user()

user_3()
"""

""" 9.4
    class Restaurant:

    def __init__(self,restaurant_name, cuisine_type,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}, an {self.cuisine_type.title()} restaurant\n")

    def open_restaurant(self):
        if self.number_served == 0:
            print(f"{self.restaurant_name.title()} is open, no costumer has been served\n")
        elif self.number_served == 1 :
            print(f"{self.restaurant_name.title()} is open, {self.number_served} costumer has been served\n")
        elif self.number_served < 0:
            print("It's impossible to have a negative number of costumers\n")
        else:  
            print(f"{self.restaurant_name.title()} is open, {self.number_served} costumers have been served\n")


def restaurant():
    my_restaurant =  Restaurant("Omelette du Fromage", "French", 0)
    my_restaurant.number_served = int(input("How many costumers have been served?: "))
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

restaurant()
"""

""" 9.5
    class User:

    def __init__(self,first_name,last_name,age, country, login_attempts):
        self.first_name = first_name
        self.last_name = last_name  
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, originally from {self.country}, was {self.age} at time of death")

    def greet_user(self):
        print(f"Greetings, {self.first_name}.\n")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login(self):
        while True:
            self.login_attempts += int(input("How many times would you like to try to login?: "))
            if self.login_attempts < 0:
                print("It's impossible to try to login a negative number of times")
                self.reset_login_attempts()
                continue
            else: 
                break

    def login_attempt(self):
        print(f"\nThere has been {self.login_attempts} login attempts")

def user_1():
    local_data = User("Albert","Einstein","76","Germany",0)
    local_data.describe_user()
    local_data.greet_user()
    local_data.increment_login()
    local_data.login_attempt()

user_1()
"""

""" 9.6
class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, a {self.cuisine_type.title()} restaurant")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name.title()} is open!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    
    def menu_flavors(self):
        print("\nWe have the following flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

flavors_available = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough"]  

def ice_cream_store():
    local_data = IceCreamStand("Cotton Candy", "Ice Cream",flavors_available)
    local_data.describe_restaurant()
    local_data.open_restaurant()
    local_data.menu_flavors()

ice_cream_store()"""

""" 9.7
    class User:

    def __init__(self,first_name,last_name,age, country):
        self.first_name = first_name
        self.last_name = last_name  
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, originally from {self.country}, was {self.age} at time of death")

    def greet_user(self):
        print(f"Greetings, {self.first_name}.\n")

def user_1():
    localData = User("Albert","Einstein","76","Germany")
    localData.describe_user()
    localData.greet_user()

#user_1()


class Admin(User):
    def __init__(self,first_name,last_name,age,country):
        super().__init__(first_name,last_name,age,country)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_admin_privileges(self):
        print("This user is an admin and has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")

def admin():
    localData = Admin("Isaac","Newton","86","UK")
    localData.describe_user()
    localData.greet_user()
    localData.show_admin_privileges()
    
admin()
 """

""" 9.8
    class User:

    def __init__(self,first_name,last_name,age, country):
        self.first_name = first_name
        self.last_name = last_name  
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, originally from {self.country}, was {self.age} at time of death")

    def greet_user(self):
        print(f"Greetings, {self.first_name}.\n")

def user_1():
    localData = User("Albert","Einstein","76","Germany")
    localData.describe_user()
    localData.greet_user()

#user_1()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nThis user is an admin and has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")

class Admin(User):
    def __init__(self,first_name,last_name,age,country):
        super().__init__(first_name,last_name,age,country)
        self.privileges = Privileges()
    
    def show_admin_privileges(self):
        self.privileges.show_privileges()

def admin():
    localData = Admin("Isaac","Newton","86","UK")
    localData.describe_user()
    localData.greet_user()
    localData.show_admin_privileges()
    
admin()
"""

""" 9.9

# The following code was copied from the Textbook
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


# This snip was added by me
    def upgrade_battery(self):
        if self.battery_size != 65:
            range = 225
            self.battery_size = 65
#Added snip ends here


class ElectricCar(Car):

    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


## Upgrade battery
print("\nAfter update: ")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
# The code coppied from the textbook, ends here"""

""" 9.13
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides
        self.roll = 10
    
    def roll_die(self):
        die_roll = 0
        print(f"\nRolling a {self.sides} die: ")
        while die_roll < self.roll:
            die_roll += 1
            roll = randint(1,self.sides)
            print(roll)


#6 sized die
my_die = Die(6)
my_die.roll_die()


#10 sized die
my_die = Die(10)
my_die.roll_die()

#20 sized die
my_die = Die(20)
my_die.roll_die()"""

from random import choice

chars = ["a","b","c","d"]

sorted_value = ""
iteration_string = ""

localValue = 0
iterations = 0

while localValue < 10:
    chars.append(str(localValue))
    localValue += 1

while len(sorted_value) < 5:
    "9.14 - Defines lottery numbers"
    sorted_value += "".join(choice(chars))

print(f"The ticket number is: {sorted_value}, any that matches it, gets an prize!")


while iteration_string != sorted_value:
    "9.15 - Check lottery with random"
    if len(iteration_string) > 4:
        iteration_string = ""
        iterations += 1
    else: 
        iteration_string += "".join(choice(chars))
        iterations += 1

print(f"It took {iterations} iterations to the value match, the loterry number was: {sorted_value}, and the matched: {iteration_string} ")