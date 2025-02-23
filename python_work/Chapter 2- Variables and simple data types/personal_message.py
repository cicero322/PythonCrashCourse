"""" Try it yourself exercises, page 63 """

"""
2-3
name = input("Enter your name: ")
greeting = f"Hello, {name}, would you like to learn python today?"
print(greeting)
"""

"""
2-4 
my_name = "Cicero"
print(my_name.upper())
print(my_name.lower())
print(my_name.title())
"""

"""
2-5 & 2-6 
quote_by = "FDR"
quote = '" The only thing we have to fear is fear itself ".'
full_quote = f" {quote_by} once famously said, : {quote}"
print(full_quote)
"""


"""
2-7
monark = "\tFrederick II\t"

print(monark)
print(monark.lstrip())
print(monark.rstrip())
print(monark.strip())
"""

#2-8
editor = ("https://nostarch.com/")
description = editor.removeprefix("https://").removesuffix(".com/")

print(f"This textbook was edit & made by {description}")