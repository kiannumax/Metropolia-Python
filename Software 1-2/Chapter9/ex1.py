class Car():
    def __init__(self, regNum, maxSpeed, currSpeed = 0, traveledDstnc = 0):
        self.regNum        = regNum
        self.maxSpeed      = maxSpeed
        self.currSpeed     = currSpeed
        self.traveledDstnc = traveledDstnc


car = Car("ABC-123", 142)

print(f"Our new car's properites are:\nRegistration Number: {car.regNum}\n"
      f"Maximum Speed: {car.maxSpeed}\nCurrent Speed: {car.currSpeed}\n"
      f"Traveled Distance: {car.traveledDstnc}")
