from app.pdf_generator.generators.comparison_pdf import *
from unittest.mock import MagicMock, call
import unittest

class ComparisonPDFTests(unittest.TestCase):

    def setUp(self):
        self.comparison_pdf = ComparisonPDF()

        self.pdf_generator_mock = MagicMock()

        self.comparison_pdf._pdf = self.pdf_generator_mock

    def test_print_player_info(self):
        self.comparison_pdf.print_player_info()

        # Add assertions to verify the expected behavior two images for the players
        self.assertTrue(self.comparison_pdf._pdf.image.called_with(
            'app/pdf_generator/resources/images/Default.png', 10, 90, 60, 60
        ))
        self.assertTrue(self.comparison_pdf._pdf.image.called_with(
            'app/pdf_generator/resources/images/Default.png', 10, 170, 60, 60
        ))

        # assert that the expected method was called with the correct arguments
        self.assertTrue(self.comparison_pdf._pdf.print_comparison_info_col1.called_with(
            self.comparison_pdf._pdf.player, self.comparison_pdf._pdf.compare
        ))

    def test_generate_pdf(self):
        # Create a sample param_map for testing
        param_map = {
            "league_data": "mock_league_data",
            "player_name": "T Clevery",
            "main_pos": "DM",
            "compare_name": "A Masina",
            "compare_pos": "FB",
            "line_plots": "mock_line_plots",
            "bar_plots": "mock_bar_plots"
        }

        # Define the expected method calls on the mock objects
        self.pdf_generator_mock.output.return_value = "Generated PDF"

        # Call the function to generate the PDF
        result = self.comparison_pdf.generate_pdf(param_map)

        # Assert the expected method calls on the mock objects
        self.pdf_generator_mock.set_info.assert_called_with("T Clevery", None, "mock_league_data", "DM")
        self.pdf_generator_mock.set_compare_info.assert_called_with("A Masina", None, "mock_league_data", "FB")
        self.pdf_generator_mock.print_comparison_title.assert_called()
        self.pdf_generator_mock.output.assert_called_with(dest='S')

        # Assert the result
        self.assertEqual(result, "Generated PDF")

if __name__ == '__main__':
    unittest.main()
