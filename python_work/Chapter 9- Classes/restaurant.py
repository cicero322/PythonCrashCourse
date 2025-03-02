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
