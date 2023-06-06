from app.graph_generator.graphs.clustered_bar_plot import *
import unittest
import pickle

class ClusteredBarPlotTests(unittest.TestCase):
    obj = None

    def set_up(self, comparison=True, comparable=True):
        player_data = {
            'Player': ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis', 'David Brown',
                       'Emma Wilson', 'Christopher Taylor', 'Olivia Anderson', 'William Martinez', 'Sophia Lee'],
            'Goals per 90': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            'Offensive duels per 90': [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
            'Defensive duels per 90': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
            'Fouls per 90': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],
            'Interceptions per 90': [70, 80, 90, 100, 10, 20, 30, 40, 50, 60],
            'Crosses per 90': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],
            'Dribbles per 90': [40, 50, 60, 70, 80, 90, 100, 10, 20, 30],
            'Progressive runs per 90': [85, 95, 105, 115, 125, 135, 145, 155, 165, 175],
            'Assists per 90': [60, 70, 80, 90, 100, 10, 20, 30, 40, 50],
            'Main position': ['CF', 'AM', 'FB', 'CB', 'ST', 'CB', 'DM', 'AM', 'ST', 'AM']
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
        if not comparable:
            param_map['compare_name'] = 'Emily Davis'
            param_map['compare_pos'] = 'Center Back'
        self.obj = ClusteredBarPlot(param_map)
        return param_map
    
    def test_color_clustered_bar_plot(self):
        randmax = 25
        param_map=self.set_up()
        ax = plt.gca()
        
        player_data = param_map['league_data']
        df=pd.DataFrame(player_data[player_data['Player'] == 'John Doe'])
        
        sns.barplot(x="Player", y='Goals per 90', data=df)

        byte1=pickle.dumps(ax)
        ax = self.obj.color_clustered_bar_plot(ax, randmax, ['Oranges', 'Blues', 'Oranges'])
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

    def draw_main_stats_plot(self):
        param_map=self.set_up()
        param_map['stats'] = ['Goals per 90', 'Defensive duels per 90', 'Crosses per 90', 'Interceptions per 90', 'Assists per 90']
        byte = None
        byte = self.obj.draw_main_stats_plot(param_map)
        self.assertNotEqual(byte,None,'no changes')

    def test_draw(self):
        param_map=self.set_up()
        param_map['stats'] = ['Goals per 90', 'Defensive duels per 90', 'Crosses per 90', 'Interceptions per 90', 'Assists per 90']
        result = self.obj.draw(param_map)
        self.assertNotEqual(pickle.dumps(result), pickle.dumps(None), 'empty graph')

    def test_draw_with_comparison_not_comparable(self):
        param_map=self.set_up(comparable=False)
        param_map['stats'] = ['Goals per 90', 'Defensive duels per 90', 'Crosses per 90', 'Interceptions per 90', 'Assists per 90']
        result = self.obj.draw(param_map)
        self.assertEqual(len(result), 2)
        for x in result:
            self.assertNotEqual(x, None, 'no graph')
            self.assertNotEqual(pickle.dumps(x), pickle.dumps(None), 'empty graph')

    def test_clustered_bar_plot_image_format(self):
        param_map=self.set_up()
        param_map['stats'] = ['Goals per 90', 'Defensive duels per 90', 'Crosses per 90', 'Interceptions per 90', 'Assists per 90']
        bytes = self.obj.draw(param_map)
        self.assertTrue(bytes.startswith(b'\x89PNG'), 'Wrong graph format. Expected PNG.')


if __name__ == '__main__':
    unittest.main()