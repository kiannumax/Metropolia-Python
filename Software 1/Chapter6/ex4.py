
def sum(ints):
    sum = 0

    for intg in ints:
        sum += int(intg)

    return sum

ints = input("Enter integers divided by a space >> ").split(" ")

print(f"The Sum of integers is: {sum(ints)}")
