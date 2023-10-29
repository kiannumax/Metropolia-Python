
zander = int(input("Enter the length of a zander in cm >> "))

if (limit := 42) <= zander:
    print("You can keep the fish!")

else:
    print(f"You should release the fish back since it is {limit - zander }cm smaller than the limit!")
