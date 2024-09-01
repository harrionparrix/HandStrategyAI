from bots import play_game, jordan_strategy, casey_strategy, alex_strategy, taylor_strategy, human_player, random_strategy, mimic_strategy, rock_player, paper_player, scissors_player
from hpx import HyperBeam, EldenRing, Maverick, DragonDance, SuperBaby
from prak import kyle_demeantrius, nostradamus, magic_mike, vladamir, hikaru
import sys
import time
from datetime import datetime, timedelta
import concurrent.futures


strategies = [
    ("HyperBeam", HyperBeam),  # hpx - HyperBeam
    ("EldenRing", EldenRing),  # hpx - EldenRing
    ("Maverick", Maverick),  # hpx - Maverick
    ("DragonDance", DragonDance),  # hpx - DragonDance
    ("SuperBaby", SuperBaby),  # hpx - SuperBaby
    ('kyle_demeantrius',kyle_demeantrius), # prak bots
    ('nostradamus',nostradamus), # prak bots
    ('magic_mike', magic_mike), # prak bots
    ('vladamir', vladamir), # prak bots
    ('hikaru', hikaru), # prak bots
    ("alex_strategy", alex_strategy),
    ("casey_strategy", casey_strategy),
    ("taylor_strategy", taylor_strategy),
    ("jordan_strategy", jordan_strategy),
    ("rock_player", rock_player),
    ("paper_player", paper_player),
    ("scissors_player", scissors_player),
    ("mimic_strategy", mimic_strategy),
    ("random_strategy", random_strategy)
]


scores = {name: 0 for name, _ in strategies}


# outer_iterations = 1000
outer_iterations = 1000
total_strategies = len(strategies)
total_pairs = total_strategies * (total_strategies - 1) // 2
total_iterations = outer_iterations * total_pairs
current_iteration = 0

def print_loader(iteration, total, start_time, bar_length=50):
    progress = iteration / total
    block = int(bar_length * progress)
    
    bar = "#" * block + "-" * (bar_length - block)
    elapsed_time = time.time() - start_time
    eta = (elapsed_time / iteration) * (total - iteration) if iteration > 0 else 0
    eta_td = timedelta(seconds=int(eta))

    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(
        f"\r[{bar}] {int(progress * 100)}% | "
        f"\nElapsed: {timedelta(seconds=int(elapsed_time))} | "
        f"ETA: {eta_td} | "
        f"Iteration: {iteration}/{total}"
    )
    sys.stdout.flush()

def evaluate_strategy_pair(pair):
    name1, strat1 = pair[0]
    name2, strat2 = pair[1]

    score1 = play_game(strat1, strat2, 1000)
    score2 = play_game(strat2, strat1, 1000)

    if score1 > score2:
        return name1, name2, 1, 0
    elif score2 > score1:
        return name1, name2, 0, 1
    else:
        return name1, name2, 0.5, 0.5



start_time = time.time()

strategy_pairs = [(strategies[i], strategies[j]) for i in range(len(strategies)) for j in range(i + 1, len(strategies))]

for _ in range(outer_iterations):

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_pair = {executor.submit(evaluate_strategy_pair, pair): pair for pair in strategy_pairs}
        
        for future in concurrent.futures.as_completed(future_to_pair):
            name1, name2, score1, score2 = future.result()
            scores[name1] += score1
            scores[name2] += score2

            current_iteration += 1
            print_loader(current_iteration, total_iterations, start_time)


ranked_strategies = sorted(scores.items(), key=lambda item: item[1], reverse=True)

print("\n\nRanking:")
for rank, (name, score) in enumerate(ranked_strategies, start=1):
    print(f"{rank}. {name} - {score} points")
print("\n\n")
