def character():
    import random
    number = random.randint(1,3)
    #Choose what happens with each number

print ("You have traveled a long way to find a temple you saw in a dream.... and it was true! You see the door in front of you.")
print ("Do you wish to enter?")
answer = input()
if answer == "yes":
    print("You chose to go in...")
    character()
if answer == "no":
    print("You chose to run away like a whimp")
