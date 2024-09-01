import random
from collections import Counter
import numpy as np
from decimal import *

getcontext().prec = 2000


# Probably uses Probability
def as25_1(prev_play, opponent_name, opponent_history=[], my_moves=[]):
    probs = [1/3, 1/3, 1/3]
    choices = ["R", "P", "S"]
    move_outcome = []
    window_size = 10
    temp_opponent_history = opponent_history[-window_size:]
    temp_my_moves = my_moves[-window_size:]
    if prev_play in choices:
        opponent_history.append(prev_play)
    else:
        opponent_history = []
        my_moves = []
    for i in range(len(temp_opponent_history)):
        prev_opp = temp_opponent_history[i]
        prev_me = temp_my_moves[i]
        
        if prev_opp == 'R':
            if prev_me == 'R':
                move_outcome.append('T')
            elif prev_me == 'P':
                move_outcome.append('W')
            else:
                move_outcome.append('L')
        elif prev_opp == 'P':
            if prev_me == 'R':
                move_outcome.append('L')
            elif prev_me == 'P':
                move_outcome.append('T')
            else:
                move_outcome.append('W')
        else:
            if prev_me == 'R':
                move_outcome.append('W')
            elif prev_me == 'P':
                move_outcome.append('L')
            else:
                move_outcome.append('T')
    
    if len(temp_opponent_history) > 0:
        for i in range(len(temp_opponent_history)):
            if not temp_opponent_history[i] in choices:
                break
            if move_outcome[i] == 'W':
                probs[choices.index(temp_my_moves[i])] *= 1.33
            elif move_outcome[i] == 'L':
                probs[choices.index(temp_my_moves[i])] *= 0.66
            else:
                probs[choices.index(temp_my_moves[i])] *= 0.9
        my_moves.append(choices[probs.index(max(probs))])
    else:
        my_moves.append(random.choice(choices))
    return my_moves[-1]

# Flippy Fibonacci
def as25_2(prev_play, opponent_name, opponent_history=[], my_moves=[]):
    choices = ["R", "P", "S"]
    if prev_play in choices:
        opponent_history.append(prev_play)
    else:
        opponent_history = []
        my_moves = []
    n_moves = len(opponent_history)
    if len(my_moves) == 0:
        my_moves.extend([0,1])
        return random.choice(["R", "P", "S"])
    my_moves.append(my_moves[-1] + my_moves[-2])
    return choices[my_moves[n_moves]%3]


def get_pi():
    pi = Decimal(3)
    for k in range(100):
        pi += Decimal(4) / (Decimal(2*k+2) * Decimal(2*k+3) * Decimal(2*k+4)) * Decimal(-1)**k
    return pi

# I'll have my Pi and eat it too
def as25_3(prev_play, opponent_name, opponent_history=[], my_moves=[]):
    choices = ["R", "P", "S"]
    if my_moves == []:
        my_moves = get_pi()
    if prev_play in choices:
        opponent_history.append(prev_play)
    else:
        opponent_history = []
    pi_str = str(my_moves)[2:]
    return choices[int(pi_str[len(opponent_history)%len(pi_str)])%3]

#Bad Bayes
def as25_4(prev_play, opponent_name, opponent_history=[], my_moves=[]):
    probs = [1/3, 1/3, 1/3]
    choices = ["R", "P", "S"]
    move_outcome = []
    window_size = 10
    temp_opponent_history = opponent_history[-window_size:]
    temp_my_moves = my_moves[-window_size:]
    if prev_play in choices:
        opponent_history.append(prev_play)
    else:
        oppponent_history = []
        my_moves = []
    for i in range(len(temp_opponent_history)):
        prev_opp = temp_opponent_history[i]
        prev_me = temp_my_moves[i]
        
        if prev_opp == 'R':
            if prev_me == 'R':
                move_outcome.append('T')
            elif prev_me == 'P':
                move_outcome.append('W')
            else:
                move_outcome.append('L')
        elif prev_opp == 'P':
            if prev_me == 'R':
                move_outcome.append('L')
            elif prev_me == 'P':
                move_outcome.append('T')
            else:
                move_outcome.append('W')
        else:
            if prev_me == 'R':
                move_outcome.append('W')
            elif prev_me == 'P':
                move_outcome.append('L')
            else:
                move_outcome.append('T')
    
    if len(temp_opponent_history) > 0:
        moves_dict = {
            "R":{
                "W":0,
                "L":0,
                "T":0
            },
            "P":{
                "W":0,
                "L":0,
                "T":0
                },
            "S":{
                "W":0,
                "L":0,
                "T":0
                }
        }
        for i in range(len(temp_my_moves)):
            moves_dict[temp_my_moves[i]][move_outcome[i]] += 1
        if(sum(moves_dict["R"].values()) == 0):
            p_r = 1/3
        else:
            p_r = moves_dict["R"]["W"]/(moves_dict["R"]["W"] + moves_dict["R"]["L"] + moves_dict["R"]["T"])
        if(sum(moves_dict["P"].values()) == 0):
            p_p = 1/3
        else:
            p_p = moves_dict["P"]["W"]/(moves_dict["P"]["W"] + moves_dict["P"]["L"] + moves_dict["P"]["T"])
        if sum(moves_dict["S"].values()) == 0:
            p_s = 1/3
        else:
            p_s = moves_dict["S"]["W"]/(moves_dict["S"]["W"] + moves_dict["S"]["L"] + moves_dict["S"]["T"])
        probs = [p_r, p_p, p_s]
        my_moves.append(choices[probs.index(max(probs))])
    else:
        my_moves.append(random.choice(choices))
    return my_moves[-1]

# Mind the Markov
def as25_5(prev_play, opponent_name, opponent_history=[], my_moves=[]):
    choices = ["R", "P", "S"]
    if prev_play in choices:
        opponent_history.append(prev_play)
    else:
        opponent_history = []
        my_moves = np.ones((3,3))
        my_moves = my_moves/3
    window_size = 10
    temp_opponent_history = opponent_history[-window_size:]
    if len(temp_opponent_history) > 10:
        moves_dict = np.zeros((3,3))
        for i in range(1, len(temp_opponent_history)):
            moves_dict[choices.index(temp_opponent_history[i-1])][choices.index(temp_opponent_history[i])] += 1
        for i in range(3):
            if sum(moves_dict[i]) == 0:
                moves_dict[i] = initial_probs
            else:
                moves_dict[i] = moves_dict[i]/sum(moves_dict[i])
        my_moves = np.matmul(moves_dict, my_moves)
        probs = my_moves[choices.index(temp_opponent_history[-1])]
        return choices[np.argmax(probs)]
    else:
        return random.choice(choices)
    return my_moves[-1]