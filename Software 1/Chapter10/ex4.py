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


class Race:
    def __init__(self, name, kms, cars):
        self.name = name
        self.kms  = kms
        self.cars = cars

    def hour_passes(self, hours):
        for car in self.cars:
            car.accelerate(randint(-10, 15))
            car.drive(hours)


    def print_status(self):
        for i in range(0, len(self.cars)):
            car = self.cars[i]

            print(f"\n{i + 1}. Car:\nRegistration Number: {car.regNum}\n"
                  f"Maximum Speed: {car.maxSpeed}\nCurrent Speed: {car.currSpeed}\n"
                  f"Traveled Distance: {car.traveledDstnc}")

    def race_finished(self):
        finished = False

        for car in self.cars:
            if car.traveledDstnc >= self.kms:
                finished = True

        return finished


cars = []

for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
print("Race has started!\n")
while not race.race_finished():
    hours += 1
    race.hour_passes(1)

    if hours % 10 == 0:
        print(f"\n\n{hours} hours had passed, here is the current status:\n")
        race.print_status()

else:
    print("\n\nRace has finished!\n")
    race.print_status()
