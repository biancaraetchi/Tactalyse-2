from papp.graph_generator.graphs.bar_plot_base import *
import unittest

class BarPlotBaseTests(unittest.TestCase):
    
    obj = None

    def set_up(self):
        self.obj = BarPlotBase()
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
            'Stat10': [95, 105, 115, 125, 135, 145, 155, 165, 175, 185]
        }
        param_map = {
            'league_data': pd.DataFrame(player_data)
        }
        return param_map

    def test_get_stats_superset(self):
        self.set_up()
        expected_list = ['Goals per 90', 'Offensive duels per 90',
                        'Defensive duels per 90', 'Fouls per 90',
                        'Interceptions per 90', 'Crosses per 90', 
                        'Dribbles per 90', 'Progressive runs per 90',
                        'Assists per 90']
        assert expected_list == self.obj.get_stats_superset(), 'incorrect list'

    def test_get_index(self):
        self.set_up()
        data = {'Player': ['John Doe', 'Jane Smith', 'Michael Johnson'],
                'Stat': [10, 20, 30]}
        df = pd.DataFrame(data)
        # Player is found in dataframe
        player_name = 'Jane Smith'
        expected_index = 1
        result = self.obj.get_index(df, player_name)
        self.assertEqual(result, expected_index, 'incorrect index')

        # Player is not found in dataframe
        with self.assertRaises(ValueError):
            self.obj.get_index(df, 'Player 4')

    def test_are_comparable(self):
        self.set_up()
        pos = 'Attacking Midfielder'
        cmp_pos = 'Winger'
        cmp_name = None
        self.assertEqual(self.obj.are_comparable(cmp_name, pos, cmp_pos), True, 'no comparison should result in True')
        cmp_name = 'Player'
        self.assertEqual(self.obj.are_comparable(cmp_name, pos, cmp_pos), True, 'positions are comparable')
        cmp_pos = 'Full Back'
        self.assertEqual(self.obj.are_comparable(cmp_name, pos, cmp_pos), False, 'positions are not comparable')
        with self.assertRaises(ValueError):
            self.obj.are_comparable(cmp_name, 'NonExistent', cmp_pos)
        with self.assertRaises(ValueError):
            self.obj.are_comparable(cmp_name, pos, 'NonExistent')

    def test_get_best_stats(self):
        param_map = self.set_up()
        stats = ['Stat1', 'Stat2', 'Stat3', 'Stat4', 'Stat5', 'Stat6', 'Stat7', 'Stat8', 'Stat9', 'Stat10']
        
        with self.assertRaises(ValueError):
            self.obj.get_best_stats(param_map, 'NonExistent', stats, len(stats)-1)

        name = 'Jane Smith'

        with self.assertRaises(ValueError):
            self.obj.get_best_stats(param_map, name, stats, len(stats)+1)
        
        expected_result = ['Stat3', 'Stat5', 'Stat9']

        result = self.obj.get_best_stats(param_map, name, stats)
        self.assertCountEqual(result, expected_result, 'incorrect best stats')

        number_of_best_statistics = 5
        expected_result = ['Stat3', 'Stat5', 'Stat9', 'Stat1', 'Stat7']
        result = self.obj.get_best_stats(param_map, name, stats, number_of_best_statistics)
        self.assertCountEqual(result, expected_result, 'incorrect best stats')


if __name__ == '__main__':
    unittest.main()