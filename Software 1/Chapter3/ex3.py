
gender = input("Enter your gender (f/m) >> ").lower()
hem    = int(input("Enter your hemoglobin level >> "))

if gender == "f":
    if hem >= 117 and hem <= 155:
        print("Your hemoglobin level is NORMAL!")

    elif hem > 155:
        print("Your hemoglobin level is HIGH!")

    else:
        print("Your hemoglobin level is LOW!")

else:
    if hem >= 134 and hem <= 167:
        print("Your hemoglobin level is NORMAL!")

    elif hem > 167:
        print("Your hemoglobin level is HIGH!")

    else:
        print("Your hemoglobin level is LOW!")
