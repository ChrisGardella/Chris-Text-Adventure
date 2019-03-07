import random

def character():
    number = random.randint(1,3)
    print (number)
    #Choose what happens with each number

def intro():
    print ("Do you wish to enter? Yes or No")
    answer = input()
    if answer == "yes" or answer == "Yes":
        print("You chose to go in...")
        character()
    elif answer == "no" or answer == "No":
        print("You chose to run away like a whimp")
        exit()
    else:
        print("I said yes or no didn't I?")
        intro()

print ("You have traveled a long way to find a temple you saw in a dream.... and it was true! You see the door in front of you.")
intro()
print("test")
