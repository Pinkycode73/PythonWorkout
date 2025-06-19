import numpy as np

def guessing_game():
    ranumb = np.random.randint(1,100)
    print(ranumb)
    guessed_answer = False
    while guessed_answer == False:
        guessed = int(input("what is your guess: "))
        if (guessed/ranumb)==1:
            guessed_answer = True
            print("Just Right")
        elif (guessed/ranumb)>1:
            print("Too High")
        elif (guessed/ranumb)<1:
            print("Too Low")
        
if __name__ == "__main__":
    guessing_game()