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
        data={axis_titles[0]:data[data.columns[column_numbers[0]]], axis_titles[1]:data[data.columns[column_numbers[1]]]}
        data=pd.DataFrame(data=data)
        sns.regplot(x=axis_titles[0], y=axis_titles[1] ,data=data)
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
