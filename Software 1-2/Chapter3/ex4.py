
year = int(input("Enter your year >> "))
leap = True

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        leap = False

else:
    leap = False


if leap:
    print(f"{year} is a leap year!")

else:
    print(f"{year} is not a leap year!")
