import random

def Game():
    print("You are welcome to the Guessing Game.")
    score = random.randint(1, 50)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print("Your score is: ", score)

    if(score > hiscore):
        print("You have set a new high score.")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            
    return score
Game()