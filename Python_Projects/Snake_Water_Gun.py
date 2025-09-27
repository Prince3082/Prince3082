# Snake, Water, Gun Game
'''
The rules of the Snake Water Gun game are as follows:
Snake vs. Water: Snake drinks water, so Snake wins.
Water vs. Gun: The gun will sink in water, so Water wins.
Snake vs. Gun: The gun will kill the snake, so Gun wins.
If both players choose the same object, the game ends in a tie. 

'''
import random

def pw(your_choise):
    if your_choise == 1:
        c = print("Your choise is snake")
    elif your_choise == 2:
        c = print("Your choise is water")
    else:
        c = print("Your choise is gun")
    return c

def cw(computer_choise):
    if computer_choise == 1:
        s = print("Computer choise is snake")
    elif your_choise == 2:
        s = print("Computer choise is water")
    else:
        s = print("Computer choise is gun")
    return s


you = {"Snake" : 1, "Water" : 2, "Gun" : 3}
computer_choise = random.choice([1, 2, 3])
your_choise = int(input("Enter your choise: "))

pw(your_choise)
cw(computer_choise)

if (computer_choise == your_choise):
    print("It's a Draw!, try again.")
else:
    if (your_choise == 1 and computer_choise == 2):
        print("You win!!")

    elif (your_choise == 1 and computer_choise == 3):
        print("You lose!")

    elif (your_choise == 2 and computer_choise == 1):
        print("You lose!")

    elif (your_choise == 2 and computer_choise == 3):
        print("You win!!")

    elif (your_choise == 3 and computer_choise == 1):
        print("You win!!")

    elif (your_choise == 3 and computer_choise == 2):
        print("You lose!")
    else:
        print("Something is going wrong")

                                                # Purely made by Prince vyas