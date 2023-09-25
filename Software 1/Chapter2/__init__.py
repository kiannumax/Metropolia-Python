num_of_excs = 6

def callExercises(num_of_excs):
    for ex in range(1, num_of_excs + 1):
        print(f"\n\tExercise {ex}:\n")
        __import__(f"ex{ex}", globals(), level = 1)

callExercises(num_of_excs)
