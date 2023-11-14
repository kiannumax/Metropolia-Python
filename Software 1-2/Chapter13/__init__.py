
ex = int(input("Since this Chapter uses Flast, program can only run 1 exercise at a time.\n"
           "Which of the 2 exercises to run? >> "))
print()

__import__(f"ex{ex}", globals(), level=1)
