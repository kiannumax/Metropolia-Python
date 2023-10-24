
num_of_excs = 4

def callExercises(num_of_excs):
    for ex in range(1, num_of_excs + 1):
        tab = ""

        if ex != 1:
            tab = "\n"

        print(f"{tab}\tExercise {ex}:\n")
        __import__(f"ex{ex}", globals(), level=1)

callExercises(num_of_excs)
