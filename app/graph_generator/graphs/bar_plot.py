import io
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from .abstract_models import Graph
from PIL import Image, ImageDraw, ImageFont

class BarPlotBase(Graph):
    __main_pos = ''
    __position_name = ''
    __orientation = 'v'
    __player_name = ''

    def draw(self, param_map):
        pass


class BarPlot(BarPlotBase):
    
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
        if len(stat_list) != 0:
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
            plt.ylabel(stat, fontsize=14)
        else:
            sns.barplot(x=stat, y=" ", data=df, orient=self.__orientation)
            plt.xlabel(stat, fontsize=14)

        plt.tight_layout()

        ax = plt.gca()
        if (self.__orientation == 'v'):
            for p in ax.patches:
                ax.text(p.get_x() + p.get_width() / 2, p.get_height(), "%0.2f" % float(p.get_height()), fontsize=12,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        else:
            for p in ax.patches:
                ax.text(p.get_width(), p.get_y() + p.get_height() / 2, "%0.2f" % float(p.get_width()), fontsize=12,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))

        ax.tick_params(axis='both', which='major', labelsize=14)

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

class MainStatsBarPlot(BarPlot):

    def __init__(self, param_map):
        param_map.update({"orientation": 'h'})
        super().__init__(param_map)
        self.__position_name = param_map.get('player_pos')
        self.__main_pos = param_map.get('main_pos')
        self.__player_name = param_map.get('player_name')
        
    def draw_clustered_bar_plot(self, param_map):
        
        matplotlib.use('agg')
        
        stats = param_map.get('stats')
        data = param_map.get('league_data')
        
        player_value_list = []
        avg_value_list = []
    
        for stat in stats:
            player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]
            stat_df = data.loc[data['Main position'] == self.__main_pos].loc[:, [stat]]
            stat_list = stat_df[stat].tolist()
            if len(stat_list) != 0:
                avg = sum(stat_list) / len(stat_list)
            else:
                avg = 0
            player_value_list.append(player_value)
            avg_value_list.append(avg)

        plt.subplot().clear()
        player_vs_avg_data = {'Statistic': stats, self.__player_name: player_value_list, 'League Average' :avg_value_list}
        df = pd.DataFrame(player_vs_avg_data)
        df = pd.melt(df, id_vars=['Statistic'], value_vars=[self.__player_name, 'League Average'], var_name='Player/Avg Value', value_name='Value')
        sns.barplot(x='Statistic', y='Value', hue='Player/Avg Value', data=df)

        new_labels = []
        for string in stats:
            new_string = string.replace('per 90', '\nper 90')
            new_labels.append(new_string)
        plt.xticks(range(len(stats)), new_labels)
        plt.xticks(fontsize=9)
        plt.tight_layout()
        
        # TODO: aggiungi label

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()
        
    def get_ranking(self, param_map):
        # TODO
        return ''

    def draw(self, param_map):
        
        stats = param_map.get('stats')
        param_map['stats'] = stats[0]

        first_bar_plot = super().draw(param_map)
        if len(stats) > 1:
            stats.pop(0)
        param_map['stats'] = stats
        clustered_bar_plot = self.draw_clustered_bar_plot(param_map)

        return [first_bar_plot, clustered_bar_plot]
        

                
        
        
        
