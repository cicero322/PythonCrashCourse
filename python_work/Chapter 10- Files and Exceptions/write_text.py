""" 10.4
from pathlib import Path

path = Path('write_text.txt')
user_input = input("Insert your name: ")

path.write_text(user_input) """

""" 10.5
from pathlib import Path

path = Path('guest_book_str.txt')

user_names = ""

while True:
    print("Insert 'q' at anytime to quit ")
    user_input = input("Insert guest name: ")

    if user_input.lower() == "q":
        break
    else:
        user_names += user_input + "\n"

path.write_text(user_names)  """



""" 10.6
try:
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    c = a / b
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You can't add a string and a number")
else:
    print(c) """

""" 10.7
from pathlib import Path

path = Path('guest_book.txt')
guests = 0

try: 
    while True:
        print("Insert 'q' at anytime to quit ")
        user_input = input("Insert a number of guests: ")
        if user_input.lower() == "q":
            break
        else:
            guests += int(user_input)
except ValueError:
    print("You're supposed to enter numbers, not letters")
else: path.write_text(str(guests))  """

""" 10.8
from pathlib import Path

cat_path = Path('cats.txt')
dog_path = Path('dogs.txt')

try:
    cat_path.read_text()
    dog_path.read_text()
except FileNotFoundError:
    print("A file is missing")
else:
    print(cat_path.read_text())
    print(dog_path.read_text()) """

""" 10.9
from pathlib import Path

cat_path = Path('cats.txt')
dog_path = Path('dogss.txt')

try:
    cat_path.read_text()
    dog_path.read_text()
except FileNotFoundError:
    pass
else:
    print(cat_path.read_text())
    print(dog_path.read_text()) """

#Using the autobiography by Benjamin Franklin

from pathlib import Path

book_path = Path("autobiography.txt")
book_read = book_path.read_text(encoding='utf=8')

istance = input("Insert the word you'd like to search: ")

count = book_read.lower().count(istance.lower())

print(f"The word '{istance}' occurs {count} times")
