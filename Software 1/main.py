
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
