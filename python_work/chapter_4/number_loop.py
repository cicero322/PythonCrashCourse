"""" Try it yourself exercises, page 98 """

""" 4-3
for number in range(1,21):
    print(number)
"""
""" 4-4
for number in range(1,1_000_000):
    print(number)
"""

""" 4-5
million = [] 

for number in range(1,1_000_001):
    million.append(number)

minimum = min(million)
maximum = max(million)
summ = sum(million)

print(minimum)
print(maximum)
print(summ)"""

""" 4-6
for odd in range(1,21,2):
    print(odd)
"""
""" 4-7
for three in range(3,21,3):
    print(three)"""

""" 4-8
for cubed in range(1,11):
    print(cubed**3)"""

""" 4-9
cubed = [cubed**3 for cubed in range(1,11)]
print(cubed)"""

"""Try it yourself exercises - page 103 """

""" 4-10
pizzas = ["margherita", "pepperoni", "four cheese", "hawaiian", "bbq chicken", "veggie", "meat lovers", "white pizza", "buffalo chicken"]

print("The first three items are:")
for pizza in pizzas[:3]:
    print(pizza.title())

print("\nThe middle three items are:")
for pizza in pizzas[3:6]:
    print(pizza.title())

print("\nThe last three items are:")
for pizza in pizzas[6:]:
    print(pizza.title())
"""

""" 4-11
pizzas = ["margherita", "pepperoni", "four cheese"]
friends_pizzas = pizzas[:]


pizzas.append("veggie")
friends_pizzas.append("hawaiian")

print("My fav' pizzas are: ")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend fav' pizzas are: ")
for pizza in friends_pizzas:
    print(pizza.title())"""

""" 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for pizza in my_foods:
    print(pizza.title())

print("\nMy friend's favorite foods are:")
for pizza in friend_foods:
    print(pizza.title())"""

""""Try it yourself exercises - Page 105"""

""" 4-13
foods = ("Pizza", "Burger", "Fries", "Pasta", "Salad")

for food in foods:
    print(food)

#foods[4] = "Mashed potatoes"
print("\nThe new menu is: ")

foods = ("Pizza", "Juice", "Fries", "Pasta", "Mashed Potatoes")
for food in foods:
    print(food)"""
