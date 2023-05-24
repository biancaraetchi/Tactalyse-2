from app.graph_generator.graphs.bar_plot import *
import unittest

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
            'Stat10': [95, 105, 115, 125, 135, 145, 155, 165, 175, 185]
        }
        param_map = {
            'league_data': pd.DataFrame(player_data),
            'player_pos': 'Striker',
            'main_pos': 'CF',
            'orientation': 'v',
            'player_name': 'John Doe',
            'compare_name': 'Jane Smith',
            'compare_pos': 'Attacking Midfielder'
        }
        self.obj = BarPlot(param_map)
        return param_map
    
    









        




if __name__ == '__main__':
    unittest.main()