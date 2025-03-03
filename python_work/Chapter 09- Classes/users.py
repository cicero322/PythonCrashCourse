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