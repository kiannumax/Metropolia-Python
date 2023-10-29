
from random import randint

rolls = int(input("How many dice to roll? >> "))
sum   = 0

for roll in range(0, rolls):
    sum += randint(1, 6)

print(f"The sum of all rolls is: {sum}")
