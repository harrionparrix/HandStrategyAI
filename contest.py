import random

def hpx1(prev_play, opponent_name, opponent_history=[]):
    if(opponent_name == "rock_player"):
        return "P"
    return ""

def hpx2(prev_play, opponent_name, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def hpx3(prev_play, opponent_name, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def hpx4(prev_play, opponent_name, opponent_history=[]):
    return random.choice(["R", "P", "S"])


def hpx5(prev_play, opponent_name, opponent_history=[]):
    return "R"