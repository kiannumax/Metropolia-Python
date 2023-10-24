class Car():
    def __init__(self, regNum, maxSpeed, currSpeed = 0, traveledDstnc = 0):
        self.regNum        = regNum
        self.maxSpeed      = maxSpeed
        self.currSpeed     = currSpeed
        self.traveledDstnc = traveledDstnc

    def accelerate(self, change):
        self.currSpeed += change

        if self.currSpeed < 0:
            self.currSpeed = 0

        elif self.currSpeed >= self.maxSpeed:
            self.currSpeed = self.maxSpeed

    def drive(self, hours):
        self.traveledDstnc += int(hours * self.currSpeed)


car = Car("ABC-123", 142, 60, 2000)

car.drive(1.5)

print(f"Car's traveled distance is: {car.traveledDstnc:d}")
