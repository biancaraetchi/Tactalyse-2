from .bar_plot import *

class ClusteredBarPlot(BarPlot):
    """
    Class that represents a clustered bar plot, that is, a bar plot with more than one bar per label
    on the x axis.
    """
    def __init__(self, param_map):
        param_map.update({"orientation": 'v'})
        super().__init__(param_map)
        self.__position_name = param_map.get('player_pos')
        self.__main_pos = param_map.get('main_pos')
        self.__player_name = param_map.get('player_name')
        self.__compare_name = param_map.get('compare_name')
        self.__compare_pos = param_map.get('compare_pos')
    

    def color_clustered_bar_plot(self, ax, max_value, cmap_list):
        """
        Function that colors the bars within the graphs with specific gradients.
        :param ax: current Axes object that allows to access and manipulate the properties of the plot's axes
        :param max_value: the value that will correspond to the darkest color in the gradient
        :param cmap_list: list of color gradients to be used for the graph. The color for each next bar
        cycles through this list.
        """
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

                grad = np.atleast_2d(np.linspace(0,1*h/max_value,256)).T
                ax.imshow(grad, extent=[x,x+w,y,y+h], origin='lower', aspect="auto", 
                          norm=cm.colors.NoNorm(vmin=0,vmax=1), cmap=plt.get_cmap(cmap_list[j]))
                

    def draw_main_stats_plot(self, param_map):
        """
        Function that draws a clustered bar plot displaying the player's main statistics and
        how they compare to the league average for their position in just one graph.
        :param param_map: set of parameters containing information about the player, the league, and the
        plot's format.
        :return: a clustered bar plot in byte form about the player's main statistics.
        """
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
            my_palette =['#B35702', '#FF0505']
        else:
            df = pd.melt(df, id_vars=['Statistic'], value_vars=[self.__player_name, self.__compare_name, 'League Average'], var_name='Player1/Player2/Avg Value', value_name='Value')
            sns.barplot(x='Statistic', y='Value', hue='Player1/Player2/Avg Value', data=df)
            my_palette =['#B35702', '#DE0030' , '#FF0505']
    
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
            cmap_list = ['YlOrBr', 'Reds']
            self.color_clustered_bar_plot(ax, max(data[stat]), cmap_list)
        else:
            cmap_list = ['YlOrBr', 'OrRd', 'Reds']
            self.color_clustered_bar_plot(ax, max(data[stat]), cmap_list)

        for y in ax.get_yticks():
            ax.axhline(y=y, linestyle='--', color='gray', alpha=0.5, zorder=-1)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()


    def draw(self, param_map):
        """
        Function that draws clustered plots and is called by the graph service. It provides 1 clustered
        bar plot if there is no comparison or the players being compared have the same main stats.
        Otherwise it displays their main stats in 2 distinct graphs. 
        :param param_map: a dictionary containing information about the player and their league.
        :return: a (list of) clustered bar plot(s) in byte form.
        """
        comparable = self.are_comparable(self.__compare_name, self.__position_name, self.__compare_pos)
        if comparable:
            stats = param_map.get('stats')
            param_map['stats'] = stats
            clustered_bar_plot = self.draw_main_stats_plot(param_map)
        else:
            print('NOT COMP')
            stats = self.get_stats_superset()
            clustered_bar_plot = []
            param_map['stats'] = stats[:4]
            clustered_bar_plot.append(self.draw_main_stats_plot(param_map))
            param_map['stats'] = stats[4:]
            clustered_bar_plot.append(self.draw_main_stats_plot(param_map))
    
        return clustered_bar_plot
    
