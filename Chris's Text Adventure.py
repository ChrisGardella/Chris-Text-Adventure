import random

def randenemy():
    enemy = random.randint(1,6)
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
        attacker = "Temple guards"
        print(attacker)
    elif enemy == 5:
        attacker = "Zombie"
        print (attacker)
    elif enemy == 6:
        attacker = "Plagued rats"
        print (attacker)

def character():
    number = random.randint(1,5)
    if number == 1:
        print("You are a wizard. You are the master of magic and are very wise.")
    elif number == 2:
        print("You are a knight! With the best armor this adventure should be nothing!")
    elif number == 3:
        print("You are a farmer, good luck.")
    elif number == 4:
        print("Your are an archer. You are a skilled bowman who rarely misses.")
    elif number == 5:
        print("You are an assassin. You are really good at killing stuff.")


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
