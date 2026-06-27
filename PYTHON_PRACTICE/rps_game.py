import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print(" ")

    playerchoice = input("Enter.. \n1 for rock,Enter... \n2 for paper,Enter... \n3 for scissor...\n\n")
    
    if playerchoice not in ["1","2","3"]:
        print("YOU must enter 1, 2 or 3")
        return play_rps()
    

    player = int(playerchoice)

    if player < 1 or player > 3 :
        sys.exit(" You must enter 1, 2 or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RPS.','')  + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.','')  + ".")
    print("")
    
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🥳 You Win"
        elif player == 2 and computer == 1:
            return "🥳 You Win"
        elif player == 3 and computer == 2:
            return "🥳 You Win"
        elif player == computer:
            return "😮Tie Game"
        else:
            return "🐍 Python wins"
    
    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count :" + str(game_count))

    #  we can this {game_count} instead of str(game_count) output will be same.

    print("\nPlay again ?")

    while True:
        playagain = input(" \nY for yes or \nQ to Quit")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
            return play_rps()
    else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋") 

play_rps()

