from app.graph_generator.graphs.bar_plot import *
import unittest
from unittest.mock import MagicMock, patch, call
import pickle
import random

class BarPlotTests(unittest.TestCase):
    
    obj = None

    def set_up(self):
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
        self.obj = BarPlot(param_map)
        return param_map

    def test_print_value_labels_vertical(self):
        self.set_up()
        ax = plt.gca()
        font_size = 8
        player_data = {' ': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)
        
        sns.barplot(x=" ", y='Stat2', data=df, orient='v')

        byte1=pickle.dumps(ax)
        ax = self.obj.print_value_labels(ax, font_size, 'v')
        byte2=pickle.dumps(ax)

        self.assertNotEqual(byte1,byte2,'no changes')

    def test_print_value_labels_horizontal(self):
        self.set_up()
        ax = plt.gca()
        font_size = 8
        player_data = {' ': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)
        
        sns.barplot(x='Stat2', y=' ', data=df, orient='h')

        byte1=pickle.dumps(ax)
        ax = self.obj.print_value_labels(ax, font_size, 'h')
        byte2=pickle.dumps(ax)

        self.assertNotEqual(byte1,byte2,'no changes')

    def test_color_graph_vertical(self):
        self.set_up()
        ax = plt.gca()
        player_data = {'Player': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)
        
        sns.barplot(x="Player", y='Stat2', data=df, orient='v')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'v', [random.random(),random.random()])
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'v', [random.random(),random.random()], False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'v', [random.random(),random.random()], True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'v', [random.random(),random.random()], True, True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'v', [random.random(),random.random()], True, False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')
        
    def test_color_graph_horizontal(self):
        self.set_up()
        ax = plt.gca()
        player_data = {'Player': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)
        
        sns.barplot(x='Stat2', y='Player', data=df, orient='h')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'h', [random.random(),random.random()])
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'h', [random.random(),random.random()], False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'h', [random.random(),random.random()], True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'h', [random.random(),random.random()], True, True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

        byte1=pickle.dumps(ax)
        ax = self.obj.color_graph(ax, random.randint(0,50), 'Oranges', 'h', [random.random(),random.random()], True, False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

    def test_draw_ticks_and_labels_vertical(self):
        self.set_up()
        player_data = {'Player': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)

        sns.barplot(x="Player", y='Stat2', data=df, orient='v')
            
        ax = plt.gca()
        byte1=pickle.dumps(ax)
        ax = self.obj.draw_ticks_and_labels(ax, 'Stat2', random.randint(0,50), False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')
        
        ax = plt.gca()
        byte1=pickle.dumps(ax)
        ax = self.obj.draw_ticks_and_labels(ax, 'Stat2', random.randint(0,50), True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')
            
    def test_draw_ticks_and_labels_horizontal(self):
        self.set_up()
        player_data = {'Player': ['John Doe'], 'Stat2': [5]}
        df=pd.DataFrame(player_data)

        sns.barplot(x='Stat2', y='Player', data=df, orient='h')
            
        ax = plt.gca()
        byte1=pickle.dumps(ax)
        ax = self.obj.draw_ticks_and_labels(ax, 'Stat2', random.randint(0,50), False)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')
        
        ax = plt.gca()
        byte1=pickle.dumps(ax)
        ax = self.obj.draw_ticks_and_labels(ax, 'Stat2', random.randint(0,50), True)
        byte2=pickle.dumps(ax)
        self.assertNotEqual(byte1,byte2,'no changes')

    def test_draw(self):
        param_map=self.set_up()
        param_map['stats'] = 'Stat2'
        bytes = None
        bytes = self.obj.draw(param_map)
        self.assertNotEqual(bytes,None,'no changes')

    def test_image_format(self):
        param_map=self.set_up()
        param_map['stats'] = 'Stat2'
        bytes = None
        bytes = self.obj.draw(param_map)
        self.assertTrue(bytes.startswith(b'\x89PNG'), 'Wrong graph format. Expected PNG.')

    def test_draw_all(self):
        param_map=self.set_up()
        param_map['stats'] = ['Stat1', 'Stat2', 'Stat3', 'Stat5', 'Stat10']
        result = self.obj.draw_all(param_map)
        self.assertEqual(len(result), len(param_map['stats'])-1)
        for x in result:
            self.assertNotEqual(x, None, 'no graph')
            self.assertNotEqual(pickle.dumps(x), pickle.dumps(None), 'empty graph')


if __name__ == '__main__':
    unittest.main()