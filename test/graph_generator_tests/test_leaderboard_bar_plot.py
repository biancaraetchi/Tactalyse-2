from app.graph_generator.graphs.leaderboard_bar_plot import *
import unittest
import pickle

class LeaderboardBarPlotTests(unittest.TestCase):
    obj = None

    def set_up(self, comparison=True):
        player_data = {
            'Player': ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis', 'David Brown',
                       'Emma Wilson', 'Christopher Taylor', 'Olivia Anderson', 'William Martinez', 'Sophia Lee'],
            'Stat1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            'Stat2': [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
            'Stat3': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
            'Stat4': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],
            'Stat5': [70, 80, 90, 100, 10, 20, 30, 40, 50, 60],
            'Stat6': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],
            'Stat7': [40, 50, 60, 70, 80, 90, 100, 10, 20, 30],
            'Stat8': [85, 95, 105, 115, 125, 135, 145, 155, 165, 175],
            'Stat9': [60, 70, 80, 90, 100, 10, 20, 30, 40, 50],
            'Stat10': [95, 105, 115, 125, 135, 145, 155, 165, 175, 185],
            'Main position': ['CF', 'AM', 'FB', 'GK', 'ST', 'CB', 'DM', 'AM', 'ST', 'AM']
        }
        param_map = {
            'league_data': pd.DataFrame(player_data),
            'player_pos': 'Striker',
            'main_pos': 'CF',
            'orientation': 'v',
            'player_name': 'John Doe',
            'compare_name': 'Jane Smith',
            'compare_pos': 'Attacking Midfielder',
        }
        if not comparison:
            param_map['compare_name'] = None
            param_map['compare_pos'] = None
        self.obj = LeaderboardBarPlot(param_map)
        return param_map
    

    def test_draw_leaderboard(self):
        param_map=self.set_up()
        param_map['stats'] = 'Stat2'
        byte = None
        byte = self.obj.draw_leaderboard(param_map)
        self.assertNotEqual(byte,None,'no changes')


    def test_draw_all_with_comparison(self):
        param_map=self.set_up()
        param_map['stats'] = ['Stat1', 'Stat3', 'Stat5', 'Stat9', 'Stat10']
        result = self.obj.draw_all(param_map)
        self.assertEqual(len(result), 6)
        for x in result:
            self.assertNotEqual(x, None, 'no graph')
            self.assertNotEqual(pickle.dumps(x), pickle.dumps(None), 'empty graph')


    def test_draw_all_without_comparison(self):
        param_map=self.set_up(False)
        param_map['stats'] = ['Stat1', 'Stat3', 'Stat5', 'Stat9', 'Stat10']
        result = self.obj.draw_all(param_map)
        self.assertEqual(len(result), 3)
        for x in result:
            self.assertNotEqual(x, None, 'no graph')
            self.assertNotEqual(pickle.dumps(x), pickle.dumps(None), 'empty graph')


if __name__ == '__main__':
    unittest.main()