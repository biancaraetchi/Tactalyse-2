from app.controller.pdf_service import PDFService
import unittest
from unittest.mock import patch


class TestPDFService(unittest.TestCase):

    def setUp(self):
        self.service = PDFService()
        self.params = {'player_name': 'bob'}

    def test_create_pdf_no_compare(self):
        with patch.object(self.service, 'create_standard_pdf', return_value='pdf') as mock_pdf:
            pdf = self.service.create_pdf(self.params)
            mock_pdf.assert_called_once_with(self.params)
            self.assertEqual('pdf', pdf)

    def test_create_pdf_compare(self):
        self.params['compare_name'] = 'joe'
        with patch.object(self.service, 'create_comparison_pdf', return_value='pdf') as mock_pdf:
            pdf = self.service.create_pdf(self.params)
            mock_pdf.assert_called_once_with(self.params)
            self.assertEqual('pdf', pdf)


if __name__ == "__main__":
    unittest.main()
