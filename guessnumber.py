import random
computerSelection = random.randint(1,30)
print(computerSelection)
while True:
    userSelection = int(input("Please enter a number in (0,100) range: "))
    if computerSelection == userSelection:
            print("Yes! You are correct!")
            break
    elif computerSelection > userSelection:
        print("Your entered number is  lower. Please enter  bigger.")
        continue
    elif userSelection > computerSelection:
        print("Your entered number is  bigger. Please enter lower.")
        continue