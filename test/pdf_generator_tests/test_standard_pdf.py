from app.pdf_generator.generators.standard_pdf import *
from unittest.mock import MagicMock, call
import unittest

class StandardPDFTests(unittest.TestCase):

    def setUp(self):
        self.standard_pdf = StandardPDF()

        self.pdf_generator_mock = MagicMock()

        self.standard_pdf._pdf = self.pdf_generator_mock

    def test_print_player_info(self):
        self.standard_pdf.print_player_info()

        # Add assertions to verify the expected behavior two images for the players
        self.assertTrue(self.standard_pdf._pdf.image.called_with(
            'app/pdf_generator/resources/images/Default.png', 55, 85, 100, 100
        ))

        # assert that the expected method was called with the correct arguments
        self.assertTrue(self.standard_pdf._pdf.print_comparison_info_col1.called_with(
            self.standard_pdf._pdf.player))

    def test_generate_pdf(self):
        # Create a sample param_map for testing
        param_map = {
            "league_data": "mock_league_data",
            "player_name": "T Clevery",
            "main_pos": "DM",
            "line_plots": "mock_line_plots",
            "bar_plots": "mock_bar_plots"
        }

        # Define the expected method calls on the mock objects
        self.pdf_generator_mock.output.return_value = "Generated PDF"

        # Call the function to generate the PDF
        result = self.standard_pdf.generate_pdf(param_map)

        # Assert the expected method calls on the mock objects
        self.pdf_generator_mock.set_info.assert_called_with("T Clevery", "mock_league_data", "DM")
        self.pdf_generator_mock.print_title.assert_called()
        self.pdf_generator_mock.output.assert_called_with(dest='S')

        # Assert the result
        self.assertEqual(result, "Generated PDF")

if __name__ == '__main__':
    unittest.main()