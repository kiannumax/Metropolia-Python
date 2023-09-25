
from random import randint

def randCombination(digits, rang):
    combination = ""

    for num in range(0, digits):
        combination += str(randint(rang[0], rang[1]))

    return combination

print(f"Random 3-digit code: {randCombination(3, (0, 9))}\n"
      f"Random 4-digit code: {randCombination(4, (1, 6))}")
