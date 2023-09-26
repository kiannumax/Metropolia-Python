
airports = {}

while True:
    usrInput = input("Enter command (quit, add, fetch) ").lower()

    if usrInput == "fetch":
        ICAO = input("Enter your existing airport's ICAO >> ")
        print(f"Airport's name is {airports[ICAO]}")

    elif usrInput == "add":
        name = input("Enter airport's name >> ")
        ICAO = input("Enter your airport's ICAO >> ")

        airports[ICAO] = name

    elif usrInput == "quit":
        break
