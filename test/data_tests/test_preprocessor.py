from app.data.preprocessors.preprocessor import Preprocessor
import unittest
import os


class TestPreprocessor(unittest.TestCase):

    def setUp(self):
        self.stat_dict = Preprocessor().league_category_dictionary()

    def test_league_stats_GK(self):
        stats = self.stat_dict.get('GK')
        expected = ['Shots blocked per 90', 'Defensive duels per 90',
                    'Interceptions per 90', 'Sliding tackles per 90',
                    'Long passes per 90', 'Dribbles per 90']
        self.assertEqual(expected, stats)

    def test_league_stats_def(self):
        stats_fb = self.stat_dict.get('FB')
        stats_cb = self.stat_dict.get('CB')
        stats_dm = self.stat_dict.get('DM')
        expected = ['Goals per 90', 'Crosses per 90',
                    'Dribbles per 90', 'Interceptions per 90',
                    'Defensive duels per 90', 'Fouls per 90']
        self.assertEqual(expected, stats_fb)
        self.assertEqual(expected, stats_cb)
        self.assertEqual(expected, stats_dm)

    def test_league_stats_atk(self):
        stats_am = self.stat_dict.get('AM')
        stats_wi = self.stat_dict.get('WI')
        expected = ['Progressive runs per 90', 'Assists per 90',
                    'Goals per 90', 'Dribbles per 90',
                    'Offensive duels per 90', 'Fouls per 90']
        self.assertEqual(expected, stats_am)
        self.assertEqual(expected, stats_wi)

    def test_league_stats_ST(self):
        stats_st = self.stat_dict.get('ST')
        expected = ['Progressive runs per 90', 'Shots per 90',
                    'Goals per 90', 'Dribbles per 90',
                    'Offensive duels per 90', 'Fouls per 90']
        self.assertEqual(expected, stats_st)


if __name__ == "__main__":
    unittest.main()
