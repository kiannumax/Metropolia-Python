
def even(ints):
    newList = []

    for intg in ints:
        if int(intg) % 2 == 0:
            newList.append(intg)

    return newList

ints = input("Enter integers divided by a space >> ").split(" ")

print(f"Original List: {ints}\nNew List: {even(ints)}")
