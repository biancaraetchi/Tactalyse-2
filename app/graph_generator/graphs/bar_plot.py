import io
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .abstract_models import Graph


class BarPlot(Graph):
    
    __position = ''
    __orientation = 'v'
    __player_name = ''


    def __init__(self, param_map):
        if 'player_pos' in param_map and not param_map['player_pos'] is None:
            self.__position = param_map.get('player_pos')
            self.__orientation = param_map.get('orientation')
            self.__player_name = param_map.get('player_name')
        
        
    def draw(self, param_map):

        data = param_map.get('league_data')
        stat = param_map.get('stats')
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

    def draw_all(self, param_map):
        stats = param_map.get('stats')
        plots = []
        for stat in stats:
            param_map['stats'] = stat
            plots.append(self.draw(param_map))
        return plots
