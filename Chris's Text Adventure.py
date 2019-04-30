# program header funstion
def program_header(title):
    import datetime
    date_object = datetime.date.today()
    print("Christopher Gardella")
    print(date_object)
    print(title)
    print("Email: 00309225@student.necc.edu")

# import random library
import random

# function that chooses a random enemy from 7 choices
def randenemy():
    enemy = random.randint(1,7)
    if enemy == 1:
        attacker = "Skeleton"
        print("A skeleton has decided to attack you!")
    elif enemy == 2:
        attacker = "Mummy"
        print("A mummy has decided to attack you!")
    elif enemy == 3:
        attacker = "Group of vampire bats"
        print("A group of vampire bats have decided to attack you!")
    elif enemy == 4:
        attacker = "Temple guards"
        print("The temple guards decided to attack you!")
    elif enemy == 5:
        attacker = "Zombie"
        print("A zombie has decided to attack you!")
    elif enemy == 6:
        attacker = "Plagued rats"
        print("Some plagued rats have decided to attack you!")
    elif enemy == 7:
        attacker = "Giant Spider"
        print("A giant spider has decided to attack you!")

# randomly chooses 1 of 5 characters
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

# function for intro, loops until someone chooses yes or no
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

# function that chooses 1 of 2 paths
def tunnelchoice():
    tunnel = input()
    if tunnel=="right" or tunnel=="Right":
        print ("You chose to go right.")
        right()
    if tunnel=="left" or tunnel=="Left":
        print ("You chose to go left.")
        left()

def fighting():
    health=10
    enemyhealth=20
    while health > 0 or enemyhealth > 0:
        playerfight = input("Attack? Yes or No?")
        healthdeduction = random.randint(0,2)
        enemydeduction = random.randint(3,5)
        if playerfight == "Yes" or playerfight == "yes":
            enemyhealth= enemyhealth- enemydeduction
            health = health - healthdeduction
            print("The enemy did",healthdeduction,"damage")
            print("You did",enemydeduction,"damage")
            if health <= 0:
                print("You have died.")
                exit()
            if enemyhealth <= 0:
                print("You defeated the enemy!")
                break
        if playerfight == "no" or playerfight == "No":
            print("You chose not to fight and the enemy killed you.")
            exit()

# Story path if you chose right hallway
def right():
    print("You walk down the dark, moss covered hallway towards a distant light.")
    print("On the way you accidentally step on a pressure plate and a section of wall closes the tunnel behind you!")
    print("No going back now....")
    trap1 = input("You start to walk towards the light. Do you check for traps? Yes or No?")
    if trap1 == "Yes" or trap1 == "yes":
        print ("You check carefully for traps and find a spike pit, you successfully avoid it and keep heading towards the light.")
    else:
        print("You decided to not check for traps and fell into a spike pit, you died...")
        exit()
    print("Once you reach the light, you find a room with already lit torches and a closed door on the other side.")
    print("You try and open the door but it wont budge. You then notice a lever on one side and a button on the other side of the door frame.")
    door = input("Do you pull the lever or push the button?")
    if door == "lever":
        print("You pull the lever. You hear a loud noise from behind the wall and the door opens. Before you can do anything an enemy appears!")
        randenemy()
    if door == "button":
        print("You push the button, nothing happens......You then pull the lever.")
        print("You hear a loud noise from behind the wall and the door opens. Before you can do anything an enemy appears!")
        randenemy()
    fighting()


# story path if you chose left hallway
def left():
    print("left")
    # this is left path

# body of program
program_header("Chris' Text Adventure")
print("")
print("You have traveled a long way to find a temple you saw in a dream.... and it was true! You see the door in front of you.")
character()
intro()
print("You light a torch and see two tunnels ahead of you. You have no indication where either of them lead. Do you go right or left?")
tunnelchoice()

