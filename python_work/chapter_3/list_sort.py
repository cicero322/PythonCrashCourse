""" 3-8

places = ["Athens", "Jerusalem", "Paris", "Singapore", "Amsterdan"]


print("I Would like to visit these cities:")
for place in places:
  print(place)

print("\nThe ordered list is:")

ordered = sorted(places)

for place in ordered:
  print(place)


print("\nThe original list remains: ")
for place in places:
  print(place)

print("\nThe reversed list is: ")
places.reverse()

for place in places:
  print(place)


places.reverse()
print("\nThe command can be undone: ")
for place in places:
  print(place)

places = sorted(places)

print("\nThe alphabetical order of the original list is: ")
for place in places:
  print(place)

places.reverse()
print("\nThe reverse of it, is: ")
for place in places:
 print(place)
"""

""" 3-9
guests =  ["Einstein", "Aristotle", "Diogenes"]
num_guest = len(guests)

print(f"The total number of guests is {num_guest}")"""


# 3-10
highest_mountains = ["Mount Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]

print(f"The {len(highest_mountains)} highest mountains are: " )

for mountain in highest_mountains:
  print(mountain)


highest_mountains.append("Cho Oyu")

print(f"\nThe {len(highest_mountains)} highest mountains are: " )

for mountain in highest_mountains:
  print(mountain)

alphabetic_order = sorted(highest_mountains)

print(f"\nThe {len(highest_mountains)} highest , not in order are:")
for mountain in alphabetic_order:
  print(mountain)
