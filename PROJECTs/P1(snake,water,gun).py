import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ")
youdict = {"s": 0, "w": 1, "g": -1}
revdict = {0: "Snake", 1: "Water", -1: "Gun"}

you = youdict[youstr]

print(f"you choose {revdict[you]} and \n computer choose {revdict[computer]}")

if(you == computer):
    print("Game is Tie")
else:
    if(you == 0 and computer == -1):
        print("You loose the game")
    elif(you == -1 and computer == 0):
        print("You win the game")
    elif(you == 1 and computer == 0):
        print("You loose the game") 
    elif(you == 0 and computer == 1):
        print("You win the game")
    elif(you == -1 and computer == 1):
        print("You loose the game")
    elif(you == 1 and computer == -1):
        print("You win the game")