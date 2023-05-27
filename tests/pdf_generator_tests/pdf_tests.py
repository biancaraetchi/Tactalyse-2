import unittest
from unittest.mock import patch, call, MagicMock
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



    @patch('app.pdf_generator.pdf.FPDF.set_font')
    @patch('app.pdf_generator.pdf.FPDF.cell')
    @patch('app.pdf_generator.pdf.FPDF.ln')
    @patch('app.pdf_generator.pdf.FPDF.image')
    def test_header(self, mock_image, mock_ln, mock_cell, mock_set_font):
        self.pdf.add_page()  # Add a new page

        self.pdf.header()

        # Assert that the expected functions are called
        expected_calls = [
        call('app/pdf_generator/resources/images/Logo_Tactalyse.png', 4, 2, 25),
        call('app/pdf_generator/resources/images/Logo_Tactalyse_Stats.png', 50, 7, 115),
        call("app/pdf_generator/resources/images/BackgroundClean.png", x=0, y=30, w=self.pdf.w, h=self.pdf.h)
        ]
        mock_image.assert_has_calls(expected_calls)
        mock_set_font.assert_called_with(self.pdf._PDF__font, 'B', 15)
        mock_cell.assert_called_with(80)
        mock_ln.assert_called_with(20)
        


    @patch("app.pdf_generator.pdf.FPDF.set_y")
    @patch("app.pdf_generator.pdf.FPDF.set_font")
    @patch("app.pdf_generator.pdf.FPDF.cell")
    def test_footer(self, mock_cell, mock_set_font, mock_set_y):
        # Call the footer method
        self.pdf.footer()

        # Assert that the set_y method is called with the expected parameters
        mock_set_y.assert_called_with(-15)

        # Assert that the set_font method is called with the expected parameters
        mock_set_font.assert_called_with(self.pdf._PDF__font, 'I', 8)
    
        # Assert that the cell method is called with the correct parameters
        mock_cell.assert_called_with(0, 10, 'Page ' + str(self.pdf.page_no()) + '/{nb}', 0, 0, 'C')





if __name__ == '__main__':
    unittest.main()
