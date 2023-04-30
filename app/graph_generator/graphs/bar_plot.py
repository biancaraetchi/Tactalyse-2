import io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from ...data import preprocessor
from .abstract_models import Graph


class BarPlot(Graph):
    
    __position = ''
    __orientation = 'v'
    __player_name = ''


    def __init__(self, player_name, player_pos, graph_type, orientation='v'):
        if player_pos:
            self.__position = player_pos
            self.__orientation = orientation
            self.__player_name = player_name
        
        
    def draw(self, data, stat):

        player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]

        stat_df = data.loc[data['Main position'] == self.__position].loc[:,[stat]]
        stat_list = stat_df[stat].tolist()
        if not (len(stat_list)==0):
            avg = sum(stat_list) / len(stat_list)
        else:
            avg = 0
        
        player_vs_avg_data = {' ': [self.__player_name, self.__position + ' league average'], stat: [player_value, avg]}       
        df = pd.DataFrame(player_vs_avg_data)
        
        plt.subplot().clear()
        sns.barplot(x=" ", y=stat, data=df, orient=self.__orientation)
        ax = plt.gca()
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width()/2, p.get_height(), "%0.2f" % float(p.get_height()), fontsize=11, color='black', ha='center', va='bottom')
        buffer = io.BytesIO()
      
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()
