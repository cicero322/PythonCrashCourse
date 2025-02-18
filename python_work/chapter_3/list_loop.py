"""" Try it yourself exercises, page 79 """

""" 3-5
guests =  ["Einstein", "Aristotle", "Diogenes"]

for guest in guests:
    print(f" Our conversation will start soon, Thank you for coming, {guest}")

print(f"It seen's that {guests[2]} won't come ")
noShow = guests.remove("Diogenes")
substitute = guests.append("Bastiat")
print(f"{guests[-1]} will replace him")
"""

""" 3-6
guests =  ["Einstein", "Aristotle", "Diogenes"]
newGuests = ["Sócrates", "Immanuel Kant", "Friedrich Nietzsche."]

for guest in guests:
    print(f" Our conversation will start soon, Thank you for coming, {guest}")

print(f"\nIt seen's that {guests[2]} won't come ")
noShow = guests.remove("Diogenes")
substitute = guests.append("Bastiat")
print(f"{guests[-1]} will replace him\n")

print("We found a new table, now the following will take part: ")
for newGuest in newGuests:
    guests.append(newGuest)

for guest in guests:
    print(f"Welcome, {guest}")"""


# 3-7

guests =  ["Einstein", "Aristotle", "Diogenes"]
newGuests = ["Sócrates", "Immanuel Kant", "Friedrich Nietzsche."]

for guest in guests:
    print(f" Our conversation will start soon, Thank you for coming, {guest}")

print(f"\nIt seen's that {guests[2]} won't come ")
noShow = guests.remove("Diogenes")
substitute = guests.append("Bastiat")
print(f"{guests[-1]} will replace him\n")

print("We found a new table, now the following will take part: ")
for newGuest in newGuests:
    guests.append(newGuest)

for guest in guests:
    print(f"Welcome, {guest}")


"""del guests[-1]
del guests[-1]
del guests[-1]
del guests[-1]"""

guests.pop()
guests.pop()
guests.pop()
guests.pop()

print("\nThe big table won't arrive in time, only two guests can be acommodated\n")

for guest in guests:
    print(f"They other guests are uninvited, but your invitation remain Mr. {guest}")

del guests[-1]
del guests[-1]

print(guests)
 















