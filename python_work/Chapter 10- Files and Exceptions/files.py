from pathlib import Path

""" 10.1
    path = Path('learning_python.txt')
print(path.read_text())

text = ""

for line in path.read_text():
    text += line

print(text) """

""" 10-2
path = Path('learning_python.txt')
content = path.read_text()
update_content = content.replace('python','rust')


text = ""

for line in update_content:
    text += line

print(text) """

""" 10.3
from pathlib import Path
path = Path('pi_digits.txt')

for line in path.read_text().splitlines():
    print(line) """

