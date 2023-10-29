from random import randint

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

cars = []

for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", randint(100, 200)))

finished = False

while not finished:
    for car in cars:
        car.accelerate(randint(-10, 15))
        car.drive(1)

        if car.traveledDstnc >= 10_000:
            finished = True

for i in range(0, 10):
    car = cars[i]

    print(f"\n{i + 1}. Car:\nRegistration Number: {car.regNum}\n"
          f"Maximum Speed: {car.maxSpeed}\nCurrent Speed: {car.currSpeed}\n"
          f"Traveled Distance: {car.traveledDstnc}")
