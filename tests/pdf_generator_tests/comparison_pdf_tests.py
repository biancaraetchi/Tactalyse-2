from app.pdf_generator.generators.comparison_pdf import *
from unittest.mock import MagicMock
import unittest

class ComparisonPDFTests(unittest.TestCase):

    def setUp(self):
        self.comparison_pdf = ComparisonPDF()

    def test_print_player_info(self):
        # Mock the comparison pdf
        self.comparison_pdf._pdf = MagicMock()

        # the method being tested
        self.comparison_pdf.print_player_info()

        # Add assertions to verify the expected behavior two images for the players
        self.assertTrue(self.comparison_pdf._pdf.image.called_with(
            'app/pdf_generator/resources/images/placeholder_player_photo.jpg', 10, 70, 60, 60
        ))
        self.assertTrue(self.comparison_pdf._pdf.image.called_with(
            'app/pdf_generator/resources/images/Foto william Troost-Ekong.jpeg', 10, 180, 60, 60
        ))

        # assert that the expected method was called with the correct arguments
        self.assertTrue(self.comparison_pdf._pdf.print_comparison_info_col1.called_with(
            self.comparison_pdf._pdf.player, self.comparison_pdf._pdf.compare
        ))

if __name__ == '__main__':
    unittest.main()
