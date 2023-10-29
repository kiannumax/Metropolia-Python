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


car = Car("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Car's current speed is: {car.currSpeed}")

car.accelerate(-200)

print(f"Car's final speed is: {car.currSpeed}")
