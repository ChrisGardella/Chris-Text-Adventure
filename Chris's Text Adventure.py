#program header funstion
def program_header(title):
    import datetime
    date_object = datetime.date.today()
    print("Christopher Gardella")
    print(date_object)
    print(title)
    print("Email: 00309225@student.necc.edu")

#import random library
import random

#function that chooses a random enemy from 7 choices
def randenemy():
    enemy = random.randint(1,7)
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
    elif enemy == 7:
        attacker = "Giant Spider"
        print (attacker)

#randomly chooses 1 of 5 characters
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

#function for intro, loops until someone chooses yes or no
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

#function that chooses 1 of 2 paths
def tunnelchoice():
    tunnel = input()
    if tunnel=="right" or tunnel=="Right":
        print ("You chose to go right.")
        right()
    if tunnel=="left" or tunnel=="Left":
        print ("You chose to go left.")
        left()

#Story path if you chose right hallway
def right():
    print("right")
    #this is for right path

#story path if you chose left hallway
def left():
    print("left")
    #this is left path

#body of program
program_header("Chris' Text Adventure")
print("")
print ("You have traveled a long way to find a temple you saw in a dream.... and it was true! You see the door in front of you.")
character()
intro()
print ("You light a torch and see two tunnels ahead of you. You have no indication where either of them lead. Do you go right or left?")
tunnelchoice()

