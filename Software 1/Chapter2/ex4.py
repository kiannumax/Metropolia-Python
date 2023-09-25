
def sum(ints):
    sum = 0

    for intg in ints:
        sum += int(intg)

    return sum

def product(ints):
    product = 1

    for intg in ints:
        product *= int(intg)

    return product

ints = input("Enter integers divided by a space >> ").split(" ")

print(f"The Sum of integers is: {sum(ints)}, Product: {product(ints)}, "
      f"and the Average: {(sum(ints) / len(ints)):.2f}")
