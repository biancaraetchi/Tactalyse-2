import io

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .abstract_models import Graph


class ScatterPlot(Graph):
    __position = ''

    def __init__(self, player_pos=None):
        if player_pos:
            self.__position = player_pos

    def draw(self, param_map):
        column_numbers = param_map.get('columns')
        data = param_map.get('player_data')
        fig, ax = plt.subplots()
        ax.clear()
        axis_titles=data.columns[column_numbers[0]].split("/")
        compare_data = param_map.get("compare_player_data")
        if isinstance(compare_data, type(None)):
            enter_data={axis_titles[0]:data[data.columns[column_numbers[0]]], axis_titles[1]:data[data.columns[column_numbers[1]]]}
            hue = None
        else:
            data["Player"] = [param_map.get('player_name')] * len(data)
            compare_data["Player"] = [param_map.get('compare_player_name')] * len(compare_data)
            necessary_data = pd.concat([data, compare_data])
            enter_data={axis_titles[0]:necessary_data[data.columns[column_numbers[0]]], axis_titles[1]:necessary_data[data.columns[column_numbers[1]]], "Player":necessary_data['Player']}
            hue = "Player"
        enter_data=pd.DataFrame(data=enter_data)
        sns.lmplot(x=axis_titles[0], y=axis_titles[1],data=enter_data, hue=hue)

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()
    
    def draw_all(self, param_map):
        columns = param_map.get('columns')
        plots = []
        for column in columns:
            param_map['columns'] = column
            plots.append(self.draw(param_map))
        return plots
