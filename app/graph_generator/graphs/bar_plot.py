from .bar_plot_base import *
                
class BarPlot(BarPlotBase):
    """
    Class that represents a bar plot comparing player(s) stats against the league average for that
    position and stat.
    """
    def __init__(self, param_map):
        if 'player_pos' in param_map and not param_map['player_pos'] is None:
            self.__position_name = param_map.get('player_pos')
            self.__main_pos = param_map.get('main_pos')
            self.__orientation = param_map.get('orientation')
            self.__player_name = param_map.get('player_name')
            self.__compare_name = param_map.get('compare_name')
            self.__compare_pos = param_map.get('compare_pos')
    

    def print_value_labels(self, ax, font_size, orientation):
        """
        Function that prints small labels on top of the bars to show the exact value of the statistic.  
        :param ax: current Axes object that allows to access and manipulate the properties of the plot's axes
        :param font_size: the labels' font size
        :param orientation: the graph's orientation. Can be vertical ('v') or horizontal ('h')
        """
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


    def color_graph(self, ax, max_value, cmap, orientation, toggle_color_bar=True):
        """
        Function that colors the bars within the graphs with a specific gradient and prints a
        color bar to the side as a legend.
        :param ax: current Axes object that allows to access and manipulate the properties of the plot's axes
        :param max_value: the value that will correspond to the darkest color in the gradient
        :param cmap: the gradient's name
        :param orientation: the graph's orientation. Can be vertical ('v') or horizontal ('h')
        """

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
        if toggle_color_bar:
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
        """
        Function that draws a bar plot given a set of parameters.
        :param param_map: set of parameters containing information about the player, the league, and the
        plot's format.
        :return: a bar plot in byte form to be displayed onto a pdf.
        """

        matplotlib.use('agg')
        comparing = (self.__compare_name != None)
        data = param_map.get('league_data')
        stat = param_map.get('stats')
        player_value = data.loc[data['Player'] == self.__player_name].iloc[0][stat]
        if comparing:
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
            ax.axhline(df[stat][1], color='#FF7700', linestyle='-.')
        else:
            ax.axhline(df[stat][2], color='#FF7700', linestyle='-.')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()


    def draw_all(self, param_map):
        """
        Function that iterates over a set of statistics and draws a bar plot for each one.
        :param param_map: set of parameters within which the stats are found.
        :return: a list of plots in byte form to be displayed onto a pdf.
        """
        comparable = self.are_comparable(self.__compare_name, self.__position_name, self.__compare_pos)
        if comparable:
            stats = param_map.get('stats')
        else:
            stats = self.get_stats_superset()

        basic_bar_plots = []
        i = 0
        for stat in stats:
            param_map['stats'] = stats[i]
            basic_bar_plots.append(self.draw(param_map))
            i += 1
        return basic_bar_plots




        
        