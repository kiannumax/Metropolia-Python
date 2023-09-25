
def talToPound(talents):
    return talents * 20

def poundToLots(pounds):
    return pounds * 32

def lotsToGramds(lots):
    return lots * 13.3


talents = float(input("Enter talents >> "))
pounds  = float(input("Enter pounds >> "))
lots    = float(input("Enter lots >> "))

grams = lotsToGramds(lots + (poundToLots(pounds + (talToPound(talents)))))

print(f"The weight in modern units:\n{grams // 1000:.0f} kilograms and {grams % 1000:.2f} grams.")
