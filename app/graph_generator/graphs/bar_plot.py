import io
import re
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns
import numpy as np
from .abstract_models import Graph
from PIL import Image, ImageDraw, ImageFont

class BarPlotBase(Graph):
    __main_pos = ''
    __position_name = ''
    __compare_pos = ''
    __orientation = 'v'
    __player_name = ''
    __compare_name = None

    def draw(self, param_map):
        pass

    def are_comparable(self, cmp_name, pos, cmp_pos):
        if cmp_name != None:
            comparable_1 = ['Attacking Midfielder', 'Winger', 'Striker']
            comparable_2 = ['Full Back', 'Center Back', 'Defensive Midfielder']
            if ((pos in comparable_1 and cmp_pos in comparable_2) or 
                (pos in comparable_2 and cmp_pos in comparable_1)):
                return False
        return True
                

class BarPlot(BarPlotBase):
    
    def __init__(self, param_map):
        if 'player_pos' in param_map and not param_map['player_pos'] is None:
            self.__position_name = param_map.get('player_pos')
            self.__main_pos = param_map.get('main_pos')
            self.__orientation = param_map.get('orientation')
            self.__player_name = param_map.get('player_name')
            self.__compare_name = param_map.get('compare_name')
            self.__compare_pos = param_map.get('compare_pos')
    

    def print_value_labels(self, ax, font_size, orientation):
        if orientation == 'h':
            for p in ax.patches:
                    ax.text(p.get_width(),  p.get_y() + (p.get_height() / 1.7) , "%0.2f" % float(p.get_width()), fontsize=font_size,
                            fontweight='bold', color='black', ha='center', va='bottom',
                            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        else:
            for p in ax.patches:
                ax.text(p.get_x() + p.get_width() / 2, p.get_height(), "%0.2f" % float(p.get_height()), fontsize=font_size,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))


    def color_graph(self, ax, max_value, cmap, orientation):

        # set up the gradient for the cmap
        grad = np.atleast_2d(np.linspace(0,1,256))

        # reestablish the plot area
        axs = ax.patches[0].axes
        lim = axs.get_xlim()+axs.get_ylim()
        axs.axis(lim)

        # color each bar
        my_cmap = plt.get_cmap(cmap)
        for bar in ax.patches:
            bar.set_edgecolor('gray')
            bar.set_facecolor("none")
            x,y = bar.get_xy()
            w, h = bar.get_width(), bar.get_height()
            if orientation == 'h':
                grad = np.atleast_2d(np.linspace(0,1*w/max_value,256))
            else:
                grad = np.atleast_2d(np.linspace(0,1*h/max_value,256)).T
            norm = cm.colors.NoNorm(vmin=0,vmax=1)
            ax.imshow(grad, extent=[x,x+w,y,y+h], origin='lower', aspect="auto", norm=norm, cmap=my_cmap)
        
        # draw color bar
        sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm)

        num_ticks = 10
        tick_values = np.linspace(0, max_value, num_ticks)
        tick_labels = []
        for x in tick_values:
            x = round(x,2)
            tick_labels.append(str(x))
        cbar.ax.set_yticklabels(tick_labels)
        cbar.set_label('Proximity to max value found within league', fontsize=8)


    def draw(self, param_map):
        matplotlib.use('agg')
        data = param_map.get('league_data')
        stat = param_map.get('stats')
        comparing = (self.__compare_name != None)
    
        player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]
        if self.__compare_name != None:
            compare_player_value = data.loc[data['Player'] == self.__compare_name].iloc[0][stat]
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

        if not comparing:
            player_vs_avg_data = {' ': [self.__player_name, avg_column_name], stat: [player_value, avg]}
        else:
            player_vs_avg_data = {' ': [self.__player_name, self.__compare_name, avg_column_name], stat: [player_value, compare_player_value, avg]}

        df = pd.DataFrame(player_vs_avg_data)

        plt.subplot().clear()
        if (self.__orientation == 'v'):
            sns.barplot(x=" ", y=stat, data=df, orient=self.__orientation)
        else:
            sns.barplot(x=stat, y=" ", data=df, orient=self.__orientation)
        
        plt.xlabel(stat, fontsize=14, fontweight='bold')
        plt.tight_layout()

        ax = plt.gca()
        self.print_value_labels(ax, 12, orientation=self.__orientation)
        ax.tick_params(axis='both', which='major', labelsize=12)

        self.color_graph(ax, max(stat_df[stat]), 'YlOrBr', self.__orientation)

        if self.__orientation == 'v':
            for y in ax.get_yticks():
                ax.axhline(y=y, linestyle='--', color='gray', alpha=0.5, zorder=-1)
        else:
            for x in ax.get_xticks():
                ax.axvline(x=x, linestyle='--', color='gray', alpha=0.5, zorder=-1)

        if not comparing:
            ax.axhline(df[stat][1], color='#FF7700', linestyle='-. -')
        else:
            ax.axhline(df[stat][2], color='#FF7700', linestyle='-.')
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
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
        param_map.update({"orientation": 'v'})
        super().__init__(param_map)
        self.__position_name = param_map.get('player_pos')
        self.__main_pos = param_map.get('main_pos')
        self.__player_name = param_map.get('player_name')
        self.__compare_name = param_map.get('compare_name')
        self.__compare_pos = param_map.get('compare_pos')
        

    def get_ranking(self, data, name):
        return data.index[data['Player'] == name][0]         


    def get_best_stats(self, param_map, name, stats):
        #stats = param_map.get('stats')
        data = param_map.get('league_data')

        rankings = []
        for stat in stats:
            data = data.sort_values(by=stat, ascending=False)
            rankings.append((self.get_ranking(data.reset_index(), name), stat))

        rankings.sort()
        rankings = rankings[:3]
        
        best_stats = []
        for x in rankings:
            best_stats.append(x[1])

        return best_stats


    def color_clustered_graph(self, ax, ydata, cmap_list, comparing):

        # set up the gradient for the cmap
        grad = np.atleast_2d(np.linspace(0,1,256))

        # reestablish the plot area
        axs = ax.patches[0].axes
        lim = axs.get_xlim()+axs.get_ylim()
        axs.axis(lim)

        for bar in ax.patches:
            bar.set_facecolor("none")
            
        # get the bars
        bars = ax.containers
        # iterate over the bars for each column
        for j in range(len(bars)):
            for i in range(len(bars[j])):

                bars[j][i].set_edgecolor('gray')

                x = bars[j][i].get_x()
                y = bars[j][i].get_y()
                h = bars[j][i].get_height()
                w = bars[j][i].get_width()

                grad = np.atleast_2d(np.linspace(0,1*h/max(ydata),256)).T
                ax.imshow(grad, extent=[x,x+w,y,y+h], origin='lower', aspect="auto", norm=cm.colors.NoNorm(vmin=0,vmax=1), cmap=plt.get_cmap(cmap_list[j]))
                

    def draw_clustered_bar_plot(self, param_map):
        
        if self.__compare_name != None:
            comparing = True
        else:
            comparing = False

        ax = plt.gca()
        matplotlib.use('agg')
        
        stats = param_map.get('stats')
        data = param_map.get('league_data')
        
        player_value_list = []
        compare_player_value_list = []
        avg_value_list = []
    
        for stat in stats:
            player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]
            if comparing:
                compare_player_value = data.loc[data['Player'] == self.__compare_name].iloc[0][stat]
            stat_df = data.loc[data['Main position'] == self.__main_pos].loc[:, [stat]]
            stat_list = stat_df[stat].tolist()
            if len(stat_list) != 0:
                avg = sum(stat_list) / len(stat_list)
            else:
                avg = 0
            player_value_list.append(player_value)
            if comparing:
                compare_player_value_list.append(compare_player_value)
            avg_value_list.append(avg)

        plt.subplot().clear()
    
        if not comparing:
            player_vs_avg_data = {'Statistic': stats, self.__player_name: player_value_list, 'League Average' :avg_value_list}
        else:
            player_vs_avg_data = {'Statistic': stats, self.__player_name: player_value_list, self.__compare_name: compare_player_value_list, 'League Average' :avg_value_list}

        df = pd.DataFrame(player_vs_avg_data)
        if not comparing:
            df = pd.melt(df, id_vars=['Statistic'], value_vars=[self.__player_name, 'League Average'], var_name='Player/Avg Value', value_name='Value')
            sns.barplot(x='Statistic', y='Value', hue='Player/Avg Value', data=df)
            my_palette =['#E45707', '#449D2B']
        else:
            df = pd.melt(df, id_vars=['Statistic'], value_vars=[self.__player_name, self.__compare_name, 'League Average'], var_name='Player1/Player2/Avg Value', value_name='Value')
            sns.barplot(x='Statistic', y='Value', hue='Player1/Player2/Avg Value', data=df)
            my_palette =['#E45707', '#3D85C6' , '#449D2B']
    
        handles, labels = ax.get_legend_handles_labels()
        new_handles = [plt.Rectangle((0,0),1,1, color=color) for color in my_palette]
        ax.legend(new_handles, labels)

        new_labels = []
        for string in stats:
            new_string = string.replace(' ', '\n').replace('90', '').replace('per', 'per 90')
            new_labels.append(new_string)
        plt.xticks(range(len(stats)), new_labels)
        plt.xticks(fontsize=9.3, fontweight='bold')
        plt.xlabel('Statistic', fontsize=0)
        plt.tight_layout()
        
        if comparing:
            self.print_value_labels(ax, 5.5, 'v')
        else:
            self.print_value_labels(ax, 8, 'v')

        if not comparing:
            cmap_list = ['YlOrBr', 'Greens']
            self.color_clustered_graph(ax, data[stat], cmap_list, comparing)
        else:
            cmap_list = ['YlOrBr', 'Blues', 'Greens']
            self.color_clustered_graph(ax, data[stat], cmap_list, comparing)

        for y in ax.get_yticks():
            ax.axhline(y=y, linestyle='--', color='gray', alpha=0.5, zorder=-1)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()
    

    def draw_leaderboard_bar_plot(self, param_map, compared_player = False):

        stat = param_map.get('stats')
        data = param_map.get('league_data')
        data = data.sort_values(by=stat, ascending=False)
        data = data.reset_index()
        max_value = max(data[stat])

        if not compared_player:
            ranking = self.get_ranking(data, self.__player_name) 
        else:
            ranking = self.get_ranking(data, self.__compare_name) 

        for i in range(len(data)):
            if i < ranking - 5 or i > ranking + 5:
                data.drop(index=i, inplace = True)

        plt.subplot().clear()
        sns.barplot(x=stat, y='Player', data=data, linewidth=0.0001)
        plt.xlim([0, max(data[stat]) + 1]) 
        plt.tight_layout()
        
        new_labels = []
        for string in data['Player']:
            if (string != self.__player_name and not compared_player) or (string != self.__compare_name and compared_player):
                new_string = string
            else:
                new_string = string + '\n(' + str(ranking) + '°)'
            new_labels.append(new_string)
        plt.yticks(range(len(data.iloc[:, 1])), new_labels)

        ax = plt.gca()
        plt.yticks(fontsize=9)
        labels = ax.get_yticklabels()
        labels[5].set_fontsize(11)
        labels[5].set_weight('bold')

        plt.xticks(fontsize=12)
        ax.xaxis.get_label().set_size(14)
        plt.ylabel('Player', fontsize=0)

        self.print_value_labels(ax, 8, 'h')
        self.color_graph(ax, max_value, 'YlOrBr', 'h')

        start = (5/6) * min(data[stat])
        end = (6/5) * max(data[stat])
        ax.set_xlim(start,end)

        for x in ax.get_xticks():
            ax.axvline(x=x, linestyle='--', color='gray', alpha=0.5, zorder=-1)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()


    def draw(self, param_map):
        
        comparable = self.are_comparable(self.__compare_name, self.__position_name, self.__compare_pos)
        if comparable:
            stats = param_map.get('stats')
        else:
            stats = ['Goals per 90', 'Offensive duels per 90',
                    'Defensive duels per 90', 'Fouls per 90',
                    'Interceptions per 90', 'Crosses per 90', 
                    'Dribbles per 90', 'Progressive runs per 90',
                    'Assists per 90']

        basic_bar_plots = []
        i = 0
        for stat in stats:
            param_map['stats'] = stats[i]
            basic_bar_plots.append(super().draw(param_map))
            i += 1

        if comparable:
            param_map['stats'] = stats
            clustered_bar_plot = self.draw_clustered_bar_plot(param_map)
        else:
            clustered_bar_plot = []
            param_map['stats'] = stats[:4]
            clustered_bar_plot.append(self.draw_clustered_bar_plot(param_map))
            param_map['stats'] = stats[4:]
            clustered_bar_plot.append(self.draw_clustered_bar_plot(param_map))

        leaderboard_bar_plots = []
        best_stats_list = self.get_best_stats(param_map, self.__player_name, stats)
        for stat in best_stats_list:
            param_map['stats'] = stat
            leaderboard_bar_plots.append(self.draw_leaderboard_bar_plot(param_map))

        if self.__compare_name != None:
            best_stats_list = self.get_best_stats(param_map, self.__compare_name, stats)
            for stat in best_stats_list:
                param_map['stats'] = stat
                leaderboard_bar_plots.append(self.draw_leaderboard_bar_plot(param_map, True))
    
        return [basic_bar_plots, clustered_bar_plot, leaderboard_bar_plots]
    


        
        