
from random import randint

def randCombination(digits, rang):
    combination = ""

    for num in range(0, digits):
        combination += str(randint(rang[0], rang[1]))

    return combination

print(f"3digit: {randCombination(3, [0, 10])} "
      f"4digit: {randCombination(4, [1, 7])}")
