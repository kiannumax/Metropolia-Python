
def getSeason(month, seasons):
    if month in (12, 1, 2):
        return seasons[0]

    elif month in (3, 4, 5):
        return seasons[1]

    elif month in (6, 7, 8):
        return seasons[2]

    elif month in (9, 10, 11):
        return seasons[3]

    else:
        return "not valid month!"


seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the number of your month >> "))

print(f"The season is: {getSeason(month, seasons)}")
