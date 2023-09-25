
attempts = 0

while attempts < 5:
    username = input("Enter your username >> ")
    password = input("Enter your password >> ")

    if username == "python" and password == "rules":
        print("Welcome!")
        break

    else:
        print("Please re-enter use info again:")
        attempts += 1

else:
    print("Access Denied!")
