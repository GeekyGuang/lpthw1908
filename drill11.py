# print("your age: ", input())
# print(input("hhhhhh"))
from sys import argv
script, userName = argv
prompt = '> '
print("Where do you live?")
live = input(prompt)
print("How old are you?")
age = input(prompt)

print(f"""
Hello, {userName},
You are {age} years old.
You live in {live}.
""")
