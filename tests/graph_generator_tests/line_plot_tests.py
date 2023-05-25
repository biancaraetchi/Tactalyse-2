from app.graph_generator.graphs.line_plot import *
import unittest

class LinePlotTests(unittest.TestCase):

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
        self.obj = LinePlot(param_map)
        return param_map

    # def test_scaled_date_value(self):
    #     param_map = self.set_up()

    #     dates = pd.to_datetime(['2019-03-17', '2019-03-18', '2019-03-27', '2019-04-01'],  format='%Y-%m-%d')
    #     self.assertEqual(self.obj.scaled_date_values(dates), 'None')

    # def test_average_entries(self):
    #     param_map = self.set_up()

    #     data_x = {'col1':[1,2,3,4,5,6,7,8]}
    #     idx_x = ['row1','row2','row3','row4','row5','row6','row7','row8']
    #     df_x = pd.DataFrame(data= data_x, index = idx_x)

    #     data_y = {'col1':[6,7,8,9,10,11,12,13]}
    #     idx_y = ['row1','row2','row3','row4','row5','row6','row7','row8']
    #     df_y = pd.DataFrame(data= data_y, index = idx_y)

    #     result_x = [0]
    #     result_y = [2]

    #     self.assertEqual(self.obj.average_entries(df_x, df_y, window=5), (result_x, result_y), 'incorrect')


        

if __name__ == '__main__':
    unittest.main()