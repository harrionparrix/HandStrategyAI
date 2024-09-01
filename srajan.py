# Description: This file contains the strategies for the Rock-Paper-Scissors game from srajan. Make your own files.
import random

global my_moves 
my_moves = []

def Avengers(prev_play, opponent_name, opponent_history=[]): #srajan
    """The core Idea is to always take revenge of a loss or prepare for the worst!"""
    # print("Avengers")
    # print(opponent_history)
    
    if prev_play == "":
        # always start with Rock
        return random.choice(["R", "P", "S"])
    elif prev_play == "R":
        # If the opponent is playing Rock last time, then there is a high probability that the opponent will anticipate Paper from us. So, we will play Scissors.
        opponent_history.append(prev_play)
        return "S"
    elif prev_play == "P":
        # If the opponent is playing Paper last time, then there is a high probability that the opponent will anticipate Scissors from us. So, we will play Rock.
        opponent_history.append(prev_play)
        return "R"
    elif prev_play == "S":
        # If the opponent is playing Scissors last time, then there is a high probability that the opponent will anticipate Rock from us. So, we will play Paper.
        opponent_history.append(prev_play)
        return "P"
    
    return "R"

def Ayanokoji(prev_play, opponent_name, opponent_history=[]): #srajan
    # print("Ayanokoji")
    # print(my_moves)
    global my_moves
    def result(your_move, opponent_move):
        if (your_move == "R" and opponent_move == "S") or (your_move == "S" and opponent_move == "P") or (your_move == "P" and opponent_move == "R"):
            return 1
        else:
            return 0
        return -1

    # First move
    if prev_play == "":
        my_moves = []
        move = random.choice(["R", "P", "S"])
        my_moves.append(move)
        return move
    
    rocks_opt = opponent_history.count("R")
    papers_opt = opponent_history.count("P")
    scissors_opt = opponent_history.count("S")

    rocks_our = my_moves.count("R")
    papers_our = my_moves.count("P")
    scissors_our = my_moves.count("S")

    # We won last time
    if (result(my_moves[-1], prev_play) == 1):
        opponent_history.append(prev_play)
        # If we won last time then We will play the move that we have played the least.
        if rocks_our == papers_opt and rocks_our == scissors_opt:
            # in this case we will play the move that has been least played by the opponent.
            if rocks_opt <= papers_opt and rocks_opt <= scissors_opt:
                my_moves.append("P")
                return "P"
            elif papers_opt <= rocks_opt and papers_opt <= scissors_opt:
                my_moves.append("S")
                return "S"
            else:
                my_moves.append("R")
                return "R"
        elif rocks_our <= papers_our and rocks_our <= scissors_our:
            my_moves.append("R")
            return "R"
        elif papers_our <= rocks_our and papers_our <= scissors_our:
            my_moves.append("P")
            return "P"
        else:
            my_moves.append("S")
            return "S"
    else:
        # If we lost last time then we will play the move that has been played the most by the opponent.
        opponent_history.append(prev_play)
        if rocks_opt >= papers_opt and rocks_opt >= scissors_opt:
            my_moves.append("P")
            return "P"
        elif papers_opt >= rocks_opt and papers_opt >= scissors_opt:
            my_moves.append("S")
            return "S"
        else:
            my_moves.append("R")
            return "R"

    return "R"
