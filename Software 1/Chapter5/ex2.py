
nums = []

while True:
    usrInput = input("Enter your number, or nothing to stop >> ")

    if not usrInput:
        if nums:
            print("Largest numbers:")
            nums.sort(reverse = True)
            
            for num in nums:
                print(num)

                if nums.index(num) == 4:
                    break

        break

    nums.append(int(usrInput))
