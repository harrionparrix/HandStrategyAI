import random
from collections import deque, defaultdict

def HyperBeam(prev_play, opponent_name, opponent_history=["R","R"]): # hpx1
    opponent_history.append(prev_play)
    if len(opponent_history) > 2:
        opponent_history.pop(0)

    guess = "R"
    if opponent_history[-1] == "R":
        guess = "P"
    elif opponent_history[-1] == "P":
        guess = "S"
    elif opponent_history[-1] == "S":
        guess = "R"

    return guess


def LRS(arr):
    n = len(arr)
    for size in range(5, 0, -1):
        temp = arr[-size:]
        for start in range(n - 2*size + 1):
            if arr[start:start+size] == temp:
                return temp
    return []

def EldenRing(prev_play, opponent_name, opponent_history=[], my_moves=[]): # hpx2
    moves = {'P': 'S', 'R': 'P', 'S': 'R'}

    if prev_play:
        opponent_history.append(prev_play)
    
    if len(opponent_history) < 10:
        move = random.choice(["R", "P", "S"])
        my_moves.append(move)
        return move
    
    if len(opponent_history) > 10:
        opponent_history.pop(0)

    if len(my_moves) > 10:
        my_moves.pop(0)
    
    pattern = LRS(opponent_history)

    if pattern:
        next_move = pattern[-1]
        move = moves[next_move] 
    else:
        move = random.choice(["R", "P", "S"])

    my_moves.append(move)
    return move


def Maverick(prev_play, opponent_name, opponent_history=[], play_order=defaultdict(int), repeat=3):
    if not prev_play:
        prev_play = random.choice(['R', 'P', 'S'])
    opponent_history.append(prev_play)

    if len(opponent_history) > repeat:
        recent_sequence = "".join(opponent_history[-repeat:])
        play_order[recent_sequence] += 1

    if len(opponent_history) > repeat:
        possible_next = ["".join(opponent_history[-repeat+1:]) + "R",
                         "".join(opponent_history[-repeat+1:]) + "P",
                         "".join(opponent_history[-repeat+1:]) + "S"]
        prediction = max(possible_next, key=lambda seq: play_order[seq])[-1]
    else:
        prediction = random.choice(['R', 'P', 'S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]

def DragonDance(prev_play, opponent_name, opponent_history=[]): # hpx4
    if prev_play:
        opponent_history.append(prev_play)
    
    if prev_play == '':
        prev_play = "R"
    moves = {'P': 'S', 'R': 'P', 'S': 'R'}
    return moves[prev_play]


def SuperBaby(prev_play, opponent_name, opponent_history=[]):  # hpx5
    
    if not prev_play:
        prev_play = "S"

    if opponent_name == "taylor_strategy":
        if len(opponent_history) == 1:
            return "S"
        else:
            moves = {'P': 'S', 'R': 'P', 'S': 'R'}
            return moves[moves[prev_play]]

    else:
        opponent_history.append(prev_play)
        
        if len(opponent_history) > 2:
            opponent_history.pop(0)

        guess = "R"
        if opponent_history[-1] == "R":
            guess = "P"
        elif opponent_history[-1] == "P":
            guess = "S"
        elif opponent_history[-1] == "S":
            guess = "R"
            
        return guess