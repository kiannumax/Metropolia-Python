
from math import pi

def unitPrice(diameter, price):
    return (price) / (pi * ((diameter / 2)**2))


rad1 = float(input("Enter first pizza's radius >> "))
rad2 = float(input("Enter second pizza's radius >> "))

price1 = float(input("Enter first pizza's price >> "))
price2 = float(input("Enter second pizza's price >> "))

if unitPrice(rad1, price1) > unitPrice(rad2, price2):
    print("Second pizza provides better quality value for money")

elif unitPrice(rad1, price1) < unitPrice(rad2, price2):
    print("First pizza provides better quality value for money")

else:
    print("Both pizzas provide same quality value for money")
