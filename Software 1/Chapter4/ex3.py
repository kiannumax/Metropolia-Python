
minNum = None
maxNum = None

while True:
    usrInput = input("Enter your number, or nothing to stop >> ")

    if not usrInput:
        if maxNum:
            print(f"Largest number: {maxNum}, and Smallest: {minNum}")

        break


    if not minNum and not maxNum:
        maxNum = minNum = usrInput
        continue


    if usrInput > maxNum:
        maxNum = usrInput

    elif usrInput < minNum:
        minNum = usrInput
