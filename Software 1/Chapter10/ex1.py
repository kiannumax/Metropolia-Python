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

hissi =  Elevator(1, 7)

hissi.go_to_floor(8)

hissi.go_to_floor(1)
