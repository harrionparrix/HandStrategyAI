import random

def hpx1(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"
    if(opponent_history[-1] == "R"):
        guess = "P"
    elif(opponent_history[-1] == "P"):
        guess = "S"
    return guess

def hpx2(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def hpx3(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def hpx4(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])


def hpx5(prev_play, opponent_history=[]):
    return "R"