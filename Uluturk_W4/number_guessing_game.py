'''
Developer: Ömer ULUTÜRK
Date: 24.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement


As a player, I want to play a game which I can guess a number the computer chooses in the range I chose.
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer.
Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is
too high or too low. If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages You can assume that the user will enter valid input.
'''

import random
from timeit import default_timer as timer
print("Would you like to play game?\nClick '1' for YES click '2' for NO")
option=int(input("Select your option:"))
tries=0

if option==1:
    start=timer()
    a = int(input("Select start of range:"))
    b = int(input("Select end of range:"))
    number = random.randint(a, b)
    print(f"You will guess a number between {a} and {b}")

    while True:
        guess = int(input("Guess a number:"))
        tries += 1
        if guess>number:
            print("Try again! Guess lower...")
        elif guess<number:
            print("Try again! Guess Higher...")
        else:
            print("You won!!!")
            end=timer()
            print(f"Number of tries: {tries}    //    time: {int(end-start)} seconds")
            break
elif option==2:
    print("Thank you!")
else:
    print("Invalid option!")