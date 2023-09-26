
# You can list multiple chapters at once by separating them by a space
# For example, '3 4' will execute exercises from chapter 3 and 4
def callChapters():
    chaps = input("Insert Chapters that you are interested in >> ").split()

    for chap in chaps:
        tab = ""

        if chaps.index(chap) == 0:
            tab = "\n"

        else:
            tab = "\n\n"

        print(f"{tab}Chapter {chap}:")
        __import__(f"Chapter{chap}")


if __name__ == "__main__":
    callChapters()
