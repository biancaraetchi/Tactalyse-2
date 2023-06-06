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

        self.pdf.set_info(player_name, "League", league_df, main_pos)

        # Assert that the player's information is correctly set
        player = self.pdf.player
        self.assertEqual(player.get_player_name(), player_name)
        self.assertEqual(player.get_player_position(), main_pos)
        self.assertEqual("League", player.get_player_league())

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

        self.pdf.set_compare_info(player_name, None, league_df, main_pos)

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

    def test_chapter_title(self):
        pdf = PDF()
        pdf.set_font = MagicMock()
        pdf.ln = MagicMock()
        pdf.cell = MagicMock()

        title = "Chapter 1"
        pdf.chapter_title(title)

        pdf.set_font.assert_called_once_with(pdf._PDF__font, '', 27)
        pdf.cell.assert_called_once_with(0, 14, title, 'B', 1, 'C', False)
        pdf.ln.assert_called_with(4)

    def test_chapter_body(self):
        pdf = PDF()
        pdf.set_font = MagicMock()
        pdf.multi_cell = MagicMock()
        pdf.ln = MagicMock()

        text = "The chapter's text body"
        pdf.chapter_body(text)

        pdf.set_font.assert_called_once_with(pdf._PDF__font, '', 12)
        pdf.multi_cell.assert_called_once_with(0, 5, text)
        pdf.ln.assert_called_once()

    def test_print_chapter(self):
        title = "Chapter 1"
        text = "The chapter's text body"

        # Mock the required methods
        self.pdf.add_page = MagicMock()
        self.pdf.chapter_title = MagicMock()
        self.pdf.chapter_body = MagicMock()
        self.pdf.set_font = MagicMock()

        # Call the method
        self.pdf.print_chapter(title, text)

        # Assert the method calls
        self.pdf.add_page.assert_called_once()
        self.pdf.chapter_title.assert_called_once_with(title)
        self.pdf.chapter_body.assert_called_once_with(text)
        self.pdf.set_font.assert_called_with('Arial', '', 12)

    def test_print_title(self):
        # Mock the required methods
        self.pdf.set_font = MagicMock()
        self.pdf.ln = MagicMock()
        self.pdf.cell = MagicMock()
        self.pdf.player.get_player_name = MagicMock(return_value="Son")

        # Call the method
        self.pdf.print_title()

        # Assert the method calls
        self.pdf.set_font.assert_called_once_with('Arial', '', 22)
        self.pdf.cell.assert_called_once_with(0, 14, "Stats Report for Son", 0, 1, 'C', False)
        self.pdf.ln.assert_called_with(4)

    def test_print_comparison_title(self):
        # Mock the required methods
        self.pdf.set_font = MagicMock()
        self.pdf.ln = MagicMock()
        self.pdf.cell = MagicMock()
        self.pdf.player.get_player_name = MagicMock(return_value="Son")
        self.pdf.compare.get_player_name = MagicMock(return_value="Haaland")

        # Call the method
        self.pdf.print_comparison_title()

        # Assert the method calls
        self.pdf.set_font.assert_called_once_with('Arial', '', 22)
        self.pdf.cell.assert_called_once_with(0, 14, "Comparison Report for Son and Haaland", 0, 1, 'C', False)
        self.pdf.ln.assert_called_with(4)
  
    def test_print_player_info_label(self):
        # Mocking the necessary methods
        self.pdf.set_text_color = MagicMock()
        self.pdf.set_xy = MagicMock()
        self.pdf.cell = MagicMock()

        # Test data
        start_x_pos = 10
        start_y_pos = 20
        end_pos = 30
        label = "Label"
        y_offset = 40
        value = "Value"

        # Call the method
        self.pdf.print_player_info_label(
            start_x_pos, start_y_pos, end_pos, label, y_offset, value
        )

        # Assertions
        self.pdf.set_text_color.assert_called_with(0, 0, 0)
        self.pdf.set_xy.assert_called_with(start_x_pos + end_pos, start_y_pos + y_offset)
        self.pdf.cell.assert_called_with(0, 20, value, ln=1)

    def test_print_comparison_info_label(self):
        # Mocking the necessary methods
        self.pdf.set_font = MagicMock()
        self.pdf.set_text_color = MagicMock()
        self.pdf.set_xy = MagicMock()
        self.pdf.cell = MagicMock()

        # Test data
        start_x_pos = 10
        start_y_pos = 20
        end_pos = 30
        label = "Label"
        y_offset = 40
        value = "Value"

        # Call the method
        self.pdf.print_comparison_info_label(
            start_x_pos, start_y_pos, end_pos, label, y_offset, value
        )

        # Assertions
        self.pdf.set_font.assert_called_once_with('Arial', 'B', 12)
        self.pdf.set_text_color.assert_called_with(0, 0, 0)
        self.pdf.set_xy.assert_called_with(start_x_pos + end_pos, start_y_pos + y_offset)
        self.pdf.cell.assert_called_with(0, 20, value, ln=1)

    def test_print_player_info_col1(self):
        pdf = PDF()
        player = MagicMock()
        player.get_player_position.return_value = 'Forward'
        player.get_player_club.return_value = 'Real Madrid'
        player.get_player_country.return_value = 'Spain'
        player.get_player_league.return_value = 'La Liga'

        pdf.print_player_info_label = MagicMock()

        pdf.print_player_info_col1(player)

        pdf.print_player_info_label.assert_any_call(52.0, 210.0, 30, 'POSITION: ', 0, 'Forward')
        pdf.print_player_info_label.assert_any_call(52.0, 210.0, 30, 'CLUB: ', 10, 'Real Madrid')
        pdf.print_player_info_label.assert_any_call(52.0, 210.0, 30, 'COUNTRY: ', 20, 'Spain')
        pdf.print_player_info_label.assert_any_call(52.0, 210.0, 30, 'LEAGUE: ', 30, 'La Liga')

    def test_print_comparison_info_col1(self):
        player = MagicMock()
        player.get_player_position.return_value = 'Forward'
        player.get_player_club.return_value = 'Real Madrid'
        player.get_player_country.return_value = 'Spain'
        player.get_player_league.return_value = 'La Liga'

        compare = MagicMock()
        compare.get_player_position.return_value = 'Midfielder'
        compare.get_player_club.return_value = 'Barcelona'
        compare.get_player_country.return_value = 'Spain'

    def test_set_plot_properties(self):
        # Test the set_plot_properties method
        self.pdf.set_plot_properties(200, 150)
        self.assertEqual(self.pdf.img_w, 200)
        self.assertEqual(self.pdf.img_h, 150)



if __name__ == '__main__':
    unittest.main()
