import unittest
from bots import play, jordan_strategy, casey_strategy, alex_strategy, taylor_strategy, mimic_strategy, rock_player, paper_player, scissors_player
from hpx import HyperBeam, EldenRing, Maverick, DragonDance, SuperBaby
import threading
import time

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Define a lock for synchronized console output
console_lock = threading.Lock()

class UnitTests(unittest.TestCase):
    player_list = [HyperBeam, EldenRing, Maverick, DragonDance, SuperBaby]  # List of bots to test

    strategies = {
        'alex_strategy': alex_strategy,
        'casey_strategy': casey_strategy,
        'taylor_strategy': taylor_strategy,
        'jordan_strategy': jordan_strategy,
        'rock_player': rock_player,
        'paper_player': paper_player,
        'scissors_player': scissors_player,
        'mimic_strategy': mimic_strategy
    }

    def run_tests_for_player(self, player):
        results = {}
        player_name = player.__name__
        print("=" * 50)
        print(f"{Colors.HEADER}{Colors.BOLD}TESTING RESULT FOR {player_name}{Colors.ENDC}")
        print("=" * 50)
        for strategy_name, strategy in self.strategies.items():
            with console_lock:
                print(f"{Colors.OKBLUE}Testing {player_name} against {strategy_name}...{Colors.ENDC}")
            
            results[strategy_name] = {}
            results[strategy_name]['results'], results[strategy_name]['win_rate'] = play(player, strategy, 1000)
            win_rate = results[strategy_name]['win_rate']
            
            with console_lock:
                if win_rate >= 60:
                    print(f"{Colors.OKGREEN}{player_name} achieved a win rate of {win_rate}% against {strategy_name}{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}{player_name} failed to achieve the desired win rate against {strategy_name}. Win rate: {win_rate}%{Colors.ENDC}")
                
                print("-" * 50)
        return player_name, results

    def test_players_vs_strategies(self):
        for player in self.player_list:
            # Run tests for the current player
            self.run_tests_for_player(player)
            
            # Wait for 5 seconds before moving to the next player
            with console_lock:
                print(f"{Colors.WARNING}Waiting for 2 seconds before testing the next player...{Colors.ENDC}")
            time.sleep(2)

if __name__ == "__main__":
    unittest.main()
