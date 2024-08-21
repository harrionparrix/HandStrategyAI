def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = "R"
    if(opponent_history[-1] == "R"):
        guess = "P"
    elif(opponent_history[-1] == "P"):
        guess = "S"
    return guess
