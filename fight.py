import unittest
from bots import play, jordan_strategy, casey_strategy, alex_strategy, taylor_strategy, mimic_strategy, rock_player, paper_player, scissors_player
from contest import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_alex_strategy(self):
        print("Testing game against alex_strategy...")
        actual = play(player, alex_strategy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat alex_strategy at least 60% of the time.')

    def test_player_vs_casey_strategy(self):
        print("Testing game against casey_strategy...")
        actual = play(player, casey_strategy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat casey_strategy at least 60% of the time.')

    def test_player_vs_taylor_strategy(self):
        print("Testing game against taylor_strategy...")
        actual = play(player, taylor_strategy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat taylor_strategy at least 60% of the time.')

    def test_player_vs_jordan_strategy(self):
        print("Testing game against jordan_strategy...")
        actual = play(player, jordan_strategy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat jordan_strategy at least 60% of the time.')

    def test_player_vs_rock_player(self):
        print("Testing game against rock_player...")
        actual = play(player, rock_player, 1000) >= 80
        self.assertTrue(
            actual,
            'Expected player to defeat rock_player at least 80% of the time.')

    def test_player_vs_paper_player(self):
        print("Testing game against paper_player...")
        actual = play(player, paper_player, 1000) >= 80
        self.assertTrue(
            actual,
            'Expected player to defeat paper_player at least 80% of the time.')

    def test_player_vs_scissors_player(self):
        print("Testing game against scissors_player...")
        actual = play(player, scissors_player, 1000) >= 80
        self.assertTrue(
            actual,
            'Expected player to defeat scissors_player at least 80% of the time.')

    def test_player_vs_mimic_strategy(self):
        print("Testing game against mimic_strategy...")
        actual = play(player, mimic_strategy, 1000) >= 80
        self.assertTrue(
            actual,
            'Expected player to defeat mimic_strategy at least 80% of the time.')

if __name__ == "__main__":
    unittest.main()
