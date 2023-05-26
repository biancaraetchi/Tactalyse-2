import unittest
import pandas as pd
from app.pdf_generator.player import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.league_df = pd.DataFrame({
            'Player': ['Son'],
            'Height': [180],
            'Age': [25],
            'Birth country': ['Korea'],
            'Weight': [75],
            'Team': ['Tottenham'],
            'Foot': ['Right'],
            'On loan': [False],
            'Contract expires': ['2024-01-01'],
            'Matches played': [20]
        })

    def test_set_personal_info(self):
        self.player.set_personal_info("Son", self.league_df)
        self.assertEqual(self.player.get_player_name(), "Son")
        self.assertEqual(self.player.get_player_height(), "180")
        self.assertEqual(self.player.get_player_age(), "25")
        self.assertEqual(self.player.get_player_country(), "Korea")
        self.assertEqual(self.player.get_player_weight(), "75")

    def test_set_football_info(self):
        self.player.set_football_info("Son", self.league_df, "Winger")
        self.assertEqual(self.player.get_player_position(), "Winger")
        self.assertEqual(self.player.get_player_club(), "Tottenham")
        self.assertEqual(self.player.get_player_league(), "ENG2")
        self.assertEqual(self.player.get_player_foot(), "Right")
        self.assertEqual(self.player.get_player_on_loan(), False)
        self.assertEqual(self.player.get_player_contract_date(), "2024-01-01")
        self.assertEqual(self.player.get_player_num_matches(), "20")

if __name__ == '__main__':
    unittest.main()
