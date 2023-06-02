import pandas as pd

from app.data.excel_reader import ExcelReader
import unittest
from unittest.mock import patch
import os


class TestExcelReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Change the CWD to the root folder
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        os.chdir(root_dir)

    def setUp(self):
        self.reader = ExcelReader()
        self.file = open('app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx', 'rb')

    def tearDown(self):
        # Clean up the files
        self.file.close()

    def test_read_file(self):
        dataframe = self.reader.read_file(self.file)
        self.assertIsInstance(dataframe, pd.DataFrame)
        self.assertIsNotNone(dataframe['Match'])
        self.assertRaises(KeyError, lambda: dataframe['Player'])

    def test_player_data(self):
        with patch.object(self.reader, 'read_file', return_value="player df") as mock_df:
            df = self.reader.player_data(self.file)
            mock_df.assert_called_once_with(self.file)
            self.assertEqual("player df", df)


if __name__ == "__main__":
    unittest.main()
