from random import randint

num = randint(1, 11)

while True:
    guess = input("Your guess >> ")

    if not guess.isnumeric():
        continue


    if int(guess) == num:
        print("Correct!")
        break

    elif int(guess) > num:
        print("Too high!")

    else:
        print("Too low!")
