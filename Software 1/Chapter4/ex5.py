
attempts = 0

while True:
    username = input("Enter your username >> ")
    password = input("Enter your password >> ")

    if username == "python" and password == "rules":
        print("Welcome!")
        break

    elif attempts == 4:
        print("Access Denied!")
        break

    else:
        print("Please re-enter use info again:")
        attempts += 1
