
cabin = input("Enter your cabin's class >> ").upper()

description = None

if cabin == "LUX":
    description = "Upper-deck cabin with a balcony."

elif cabin == "A":
    description = "Above the car deck, equipped with a window."

elif cabin == "B":
    description = "Windowless cabin above the car deck."

elif cabin == "C":
    description = "Windowless cabin below the car deck."

else:
    print("Invalid cabin class!")


if description:
    print(f"Your cabin's decription:\n{description}")
