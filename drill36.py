from sys import argv
from sys import exit
script, name = argv

def math_quiz():
    print("Welcome to math quiz")
    print("1. addition 2. multiply")
    choice = int(input("> "))

    if choice == 1:
        print("1 + 2 = ?")
        answer = int(input('> '))
        if answer == 3:
            print("Well done!")
            exit(0)
        else:
            dead("Wrong!")
    elif choice == 2:
        print("2 * 3 = ?")
        answer = int(input('> '))
        if answer == 6:
            print("Well Done!")
            exit(0)
        else:
            dead("Wrong!")
    else:
        dead("Sorry, no other choice.")

def Chinese_quiz():
    poem = ["清风徐来", "水波不兴"]

    print("清风徐来的下一句是什么？")
    while True:
        answer = input('> ')
        right = 0
        for i in poem:
            if answer == i:
                right = 1
        if right:
            print("Well Done!")
            exit(0)
        else:
            print("Wrong! Do you want to try again?")
            answer = input("> ")
            if 'y' in answer:
                print("Good!")
            else:
                dead("see you!")
        

def dead(error):
    print(error, "Good job!")
    exit(0)

def start(name):
    print(F"Hello, {name}")
    print("What major are you good at?")
    
    while True:
        choice = input("> ")

        if "math" in choice:
            math_quiz()
        elif "Chinese" in choice:
            Chinese_quiz()
        else:
            print("Sorry, no such choice, please try again.")

start(name)