import random

def randenemy():
    enemy = random.randint(1,5)
    if enemy == 1:
        attacker = "Skeleton"
        print(attacker)
    elif enemy == 2:
        attacker = "Mummy"
        print(attacker)
    elif enemy == 3:
        attacker = "Group of vampire bats"
        print(attacker)
    elif enemy == 4:
        attacker = "Temple gaurds"
        print(attacker)
    elif enemy == 5:
        attacker = "Zombie"
        print (attacker)

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
randenemy()
