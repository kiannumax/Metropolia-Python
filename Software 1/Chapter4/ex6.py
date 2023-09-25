
from random import uniform

N = int(input("How many random points to generate? >> "))

n = 0
i = 0

while i <= N:
    x = uniform(-1.000, 1.000)
    y = uniform(-1.000, 1.000)

    if ((x**2) + (y**2)) < 1:
        n += 1

    i += 1

print(f"Pi's approximation: {((4 * n) / N):.3f}")
