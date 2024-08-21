from bots import play_game, jordan_strategy, casey_strategy, alex_strategy, taylor_strategy, human_player, random_strategy, mimic_strategy, rock_player, paper_player, scissors_player
from contest import player, player2


strategies = [
    ("player", player), # add unique name and function
    ("player2", player2), # add unique name and function
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

for i in range(len(strategies)):
    for j in range(i + 1, len(strategies)):
        name1, strat1 = strategies[i]
        name2, strat2 = strategies[j]
        
        score1 = play_game(strat1, strat2, 1000)
        score2 = play_game(strat2, strat1, 1000)

        if score1 > score2:
            scores[name1] += 1
        elif score2 > score1:
            scores[name2] += 1
        else:
            scores[name1] += 0.5
            scores[name2] += 0.5


ranked_strategies = sorted(scores.items(), key=lambda item: item[1], reverse=True)

print("\n\nRanking:")
for rank, (name, score) in enumerate(ranked_strategies, start=1):
    print(f"{rank}. {name} - {score} points")
print("\n\n")
