import unittest
from flask import Response
from app.controller.app import app
import os


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Change the CWD to the root folder
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        os.chdir(root_dir)

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        # Create mock files and data
        self.league_file = open('app/pdf_generator/resources/test_data/ENG2.xlsx', 'rb')
        self.player_file = open('app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx', 'rb')
        self.compare_file = open('app/pdf_generator/resources/test_data/Player stats I. Sarr.xlsx', 'rb')
        self.player_image = open("app/pdf_generator/resources/images/Default.png", 'rb')
        self.player_cmp_image = open("app/pdf_generator/resources/images/Default.png", 'rb')
        self.player_name = 'T. Cleverley'
        self.compare_name = 'A. Masina'
        self.start_date = '2023-01-01'
        self.end_date = '2023-06-01'

    def tearDown(self):
        pass

    def check_assertions(self, response):
        # Assert the response
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/pdf')
        self.assertIsInstance(response.data, bytes)

        # Clean up the files
        self.league_file.close()
        self.player_file.close()
        self.compare_file.close()
        self.player_image.close()
        self.player_cmp_image.close()

    def test_pdf_endpoint(self):

        # Make a POST request to the endpoint
        response = self.app.post('/pdf',
                                 data={
                                     'league-file': (self.league_file, 'league_file.xlsx'),
                                     'player-file': (self.player_file, 'player_file.xlsx'),
                                     'compare-file': (self.compare_file, 'compare_file.xlsx'),
                                     'player-name': self.player_name,
                                     'compare-name': self.compare_name,
                                     'start-date': self.start_date,
                                     'end-date': self.end_date,
                                     'player-image': (self.player_image, 'player_image.png'),
                                     'player-cmp-image': (self.player_cmp_image, 'player_cmp_image.png')
                                 },
                                 content_type='multipart/form-data')
        self.check_assertions(response)


if __name__ == '__main__':
    unittest.main()
