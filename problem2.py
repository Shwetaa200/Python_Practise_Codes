import random

def game():
    print("You are Playing the game....")
    score = random.randint(1,62)
    # fetch the highscore
    with open("highscore.txt") as f:
            highscore=f.read()
            if(highscore==" "):
                highscore = int(highscore)
            else:
                highscore=0
    print(f"Your Score: {score}")
    if(score>highscore):
        # write this highscore in the file
        with open("highscore.txt","w") as f:
            f.write(str(score))
        return score
game()
