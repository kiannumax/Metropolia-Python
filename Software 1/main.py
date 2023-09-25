
def callChapters():
    chaps = input("Insert Chapters that you are interested in >> ").split()


    for chap in chaps:
        print(f"\n\nChapter {chap}:")
        __import__(f"Chapter{chap}")


if __name__ == "__main__":
    callChapters()
