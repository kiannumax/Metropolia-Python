
while True:
    inches = float(input("Enter the value in inches >> "))

    if inches < 0:
        break

    print(f"The value in cm: {(inches * 2.54):.2f} ")
