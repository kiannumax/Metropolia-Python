
names = set()

while True:
    usrInput = input("Enter a name >> ")

    if not usrInput:
        for name in names:
            print(name)

        break

    print(usrInput)
    names.add(usrInput)
