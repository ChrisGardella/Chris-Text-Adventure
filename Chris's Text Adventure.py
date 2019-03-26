import random

def character():
    number = random.randint(1,3)
    if number == 1:
        print("You are a wizard. You are the master of magic and are very wise.")
    elif number == 2:
        print("You are a brave knight! With the best armor and sword in the land this should be nothing!")
    elif number == 3:
        print("You are a farmer, good luck.")


def intro():
    print ("Do you wish to enter? Yes or No")
    answer = input()
    if answer == "yes" or answer == "Yes":
        print("You chose to go in...")
    elif answer == "no" or answer == "No":
        print("You chose to run away like a whimp.")
        exit()
    else:
        print("I said yes or no didn't I?")
        intro()

print ("You have traveled a long way to find a temple you saw in a dream.... and it was true! You see the door in front of you.")
character()
intro()

