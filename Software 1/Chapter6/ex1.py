
from random import randint

def rollDice():
    return randint(1, 6)

while True:
    print(roll := rollDice())

    if roll == 6:
        print("Done!")
        break
