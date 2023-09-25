
def galToLit(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("Enter the volume in gallons >> "))

    if gallons < 0:
        break

    print(f"The volume in liters: {(galToLit(gallons)):.2f} ")
