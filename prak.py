import random

def vladamir(prev_opponent_play,opponent_name, my_history = []):
    move = random.randint(1,3)
    if  move == 1:
        return 'R'
    elif move == 2:
        return 'P'
    else:
        return 'S'
    
def magic_mike(prev_opponent_play,opponent_name, my_history = []):
    # print('Think of a number, any number')
    # print('Multiply it by 6, add 1 to it, multiply that number by 3, subtract 2 from it')
    # print('Add 1 less than the number your original number to it, multiply this by 3')
    # print('Divide by 19 times your original number')
    # print('Is the number you have in your head 3, well well time to choose scissors?') 
    
    x = random.randint(1,1000)
    a = (1 + 6*x)*3 -2
    a = (a + x-1)*3
    a /= 19*x
    print(x)
    print(a)    
    if  a == 1:
        return 'R'
    elif a == 2:
        return 'P'
    else:
        return 'S'
    
def nostradamus(prev_opponent_play,opponent_name, my_history = []):
    move = 'P'
    if len(my_history) != 0:
        if(my_history[-1]) == 'R':
            move = 'P'
        elif(my_history[-1]) == 'P':
            move = 'S'
        else: 
            move = 'R'
    my_history.append(prev_opponent_play)
    return move

def kyle_demeantrius(prev_opponent_play,opponent_name, my_history = []):
    moves = {'R': 1, 'P':2, 'S': 3}
    moves_rev = {1:'R', 2: 'P',3: 'S'}
    avg = 0
    for i in my_history:
        try:
            avg += moves[i]
        except:
            avg += 1
    my_history.append(prev_opponent_play)
    avg /= len(my_history)
    avg = round(avg)
        
    if avg != 0:
        return moves_rev[avg] 
    else:
        return 'P'

def hikaru(prev_opponent_play, opponent_name,my_history = []):
    global hikaru_cnt
    pre_moves = 'PPPPPPPRRRRRRRRRPPPPRPPRPRPRPRPRRRRSSSSSPPRPRPPSPSPSSSSSSPRPSPPSPRPRPRPPSPRPSPPSPRPPPPRRRRSSSRPSPRPPPPPPPRPPRRRSSRSRSRRSRSRSRPRSPRSPRPRSPRSPRSPPPPPPPRRSRRRSSSSS'
    try :
        hikaru_cnt +=1
        pass
    except:
        hikaru_cnt = 0
    hikaru_cnt +=1
    if(hikaru_cnt >= len(pre_moves)):
        hikaru_cnt = 0
            
    move = pre_moves[hikaru_cnt]
    return move

    