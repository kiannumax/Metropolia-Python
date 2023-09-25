
from random import randint

def rollDice(sides):
    return randint(1, sides)

sides = int(input("How many sides on a dice? >> "))

while True:
    print(roll := rollDice(sides))

    if roll == sides:
        print("Done!")
        break
