from bots import play, jordan_strategy, casey_strategy, alex_strategy, taylor_strategy, human_player, random_strategy, mimic_strategy, rock_player, paper_player, scissors_player
from hpx import HyperBeam, EldenRing, Maverick, DragonDance, SuperBaby


strategies = [
    ("HyperBeam", HyperBeam),  # hpx - HyperBeam
    ("EldenRing", EldenRing),  # hpx - EldenRing
    ("Maverick", Maverick),  # hpx - Maverick
    ("DragonDance", DragonDance),  # hpx - DragonDance
    ("SuperBaby", SuperBaby),  # hpx - SuperBaby
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

for i in range(1,len(strategies)):
    name1, strat1 = strategies[0]
    name2, strat2 = strategies[i]
    
    play(strat1, strat2, 1000)
