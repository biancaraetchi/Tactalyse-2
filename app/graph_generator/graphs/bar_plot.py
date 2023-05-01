import io

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .abstract_models import Graph


class BarPlot(Graph):
    __main_pos = ''
    __position_name = ''
    __orientation = 'v'
    __player_name = ''

    def __init__(self, param_map):
        if 'player_pos' in param_map and not param_map['player_pos'] is None:
            self.__position_name = param_map.get('player_pos')
            self.__main_pos = param_map.get('main_pos')
            self.__orientation = param_map.get('orientation')
            self.__player_name = param_map.get('player_name')

    def draw(self, param_map):
        matplotlib.use('agg')
        data = param_map.get('league_data')
        stat = param_map.get('stats')
        player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]

        stat_df = data.loc[data['Main position'] == self.__main_pos].loc[:, [stat]]
        stat_list = stat_df[stat].tolist()
        if not (len(stat_list) == 0):
            avg = sum(stat_list) / len(stat_list)
        else:
            avg = 0

        if (self.__orientation == 'v'):
            avg_column_name = self.__position_name + ' \nleague average'
        else:
            avg_column_name = self.__position_name.replace(' ', '\n') + ' \nleague \naverage'

        player_vs_avg_data = {' ': [self.__player_name, avg_column_name], stat: [player_value, avg]}
        df = pd.DataFrame(player_vs_avg_data)

        plt.subplot().clear()
        if (self.__orientation == 'v'):
            sns.barplot(x=" ", y=stat, data=df, orient=self.__orientation)
        else:
            sns.barplot(x=stat, y=" ", data=df, orient=self.__orientation)

        plt.tight_layout()

        ax = plt.gca()
        if (self.__orientation == 'v'):
            for p in ax.patches:
                ax.text(p.get_x() + p.get_width() / 2, p.get_height(), "%0.2f" % float(p.get_height()), fontsize=11,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        else:
            for p in ax.patches:
                ax.text(p.get_width(), p.get_y() + p.get_height() / 2, "%0.2f" % float(p.get_width()), fontsize=11,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))

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
