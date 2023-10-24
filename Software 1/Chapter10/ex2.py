class Elevator:
    def __init__(self, botmFloor, topFloor):
        self.topFloor  = topFloor
        self.botmFloor = self.currFloor = botmFloor

    def go_to_floor(self, floor):
        if floor not in range(self.botmFloor, self.topFloor + 1):
            print("Floor not in range!")
            return

        elif self.currFloor == floor:
            print("Elevator is already on that floor!")
            return

        while self.currFloor != floor:
            print(f"Elevator is currently on the floor {self.currFloor}")

            if self.currFloor < floor:
                self.floor_up()
            else:
                self.floor_down()
        else:
            print(f"Elevator has reached the floor {floor}\n")

    def floor_up(self):
        self.currFloor += 1

    def floor_down(self):
        self.currFloor -= 1

class Building:
    def __init__(self, botmFloor, topFloor, elevatorsNum):
        self.elevators = []

        for i in range(0, elevatorsNum):
            self.elevators.append(Elevator(botmFloor, topFloor))

    def run_elevator(self, elevatorNum, floor):
        print(f"Elevator {elevatorNum} is running:\n")
        self.elevators[elevatorNum].go_to_floor(floor - 1)

building = Building(1, 7, 3)

building.run_elevator(2, 4)
