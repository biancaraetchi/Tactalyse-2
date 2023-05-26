import unittest
from unittest.mock import patch
import pandas as pd
from io import StringIO
from PIL import Image
from fpdf import FPDF
from app.pdf_generator.player import Player
from app.pdf_generator.pdf import PDF


class TestPDF(unittest.TestCase):

    def setUp(self):
        self.pdf = PDF()

    def test_set_info(self):
        player_name = "T Clevery"
        league_df = pd.DataFrame({
            'Player': ['T Clevery'],
            'Height': [180],
            'Age': [25],
            'Birth country': ['England'],
            'Weight': [75],
            'Team': ['Temp'],
            'Foot': ['Right'],
            'On loan': [False],
            'Contract expires': ['2024-01-01'],
            'Matches played': [20]
        })
        main_pos = "DM"

        self.pdf.set_info(player_name, league_df, main_pos)

        # Assert that the player's information is correctly set
        player = self.pdf.player
        self.assertEqual(player.get_player_name(), player_name)
        self.assertEqual(player.get_player_position(), main_pos)

        # Assert that the player's football info is set using the mock DataFrame

    def test_set_compare_info(self):
        player_name = "A Masina"
        league_df = pd.DataFrame({
            'Player': ['A Masina'],
            'Height': [180],
            'Age': [25],
            'Birth country': ['Morocco'],
            'Weight': [75],
            'Team': ['Temp'],
            'Foot': ['Right'],
            'On loan': [False],
            'Contract expires': ['2024-01-01'],
            'Matches played': [20]
        })
        main_pos = "FB"

        self.pdf.set_compare_info(player_name, league_df, main_pos)

        # Assert that the compare player's information is correctly set
        compare = self.pdf.compare
        self.assertEqual(compare.get_player_name(), player_name)
        self.assertEqual(compare.get_player_position(), main_pos)

        # Assert that the compare player's football info is set using the mock DataFrame


if __name__ == '__main__':
    unittest.main()
