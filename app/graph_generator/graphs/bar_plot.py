import io

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import cm

from .bar_plot_base import BarPlotBase


class BarPlot(BarPlotBase):
    """
    Class that represents a bar plot comparing player(s) stats against the league average for that
    position and stat.
    """

    def __init__(self, param_map):
        if 'player_pos' in param_map and param_map['player_pos'] is not None:
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
        :return: modified Axes object.
        """
        if orientation == 'h':
            for p in ax.patches:
                ax.text(p.get_width(), p.get_y() + (p.get_height() / 1.7), "%0.2f" % float(p.get_width()),
                        fontsize=font_size,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        else:
            for p in ax.patches:
                ax.text(p.get_x() + p.get_width() / 2, p.get_height(), "%0.2f" % float(p.get_height()),
                        fontsize=font_size,
                        fontweight='bold', color='black', ha='center', va='bottom',
                        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))
        return ax

    def color_graph(self, ax, max_value, cmap, orientation, offset, toggle_color_bar=True, leaderboard=False):
        """
        Function that colors the bars within the graphs with a specific gradient and prints a
        color bar to the side as a legend.
        :param ax: current Axes object that allows to access and manipulate the properties of the plot's axes
        :param max_value: the value that will correspond to the darkest color in the gradient
        :param cmap: the gradient's name
        :param orientation: the graph's orientation. Can be vertical ('v') or horizontal ('h')
        :param offset:
        :param toggle_color_bar:
        :param leaderboard:
        :return: modified Axes object.
        """

        # reestablish the plot area
        axs = ax.patches[0].axes
        lim = axs.get_xlim() + axs.get_ylim()
        axs.axis(lim)

        # color each bar
        my_cmap = plt.get_cmap(cmap)
        for bar in ax.patches:
            bar.set_edgecolor('gray')
            bar.set_facecolor("none")
            x, y = bar.get_xy()
            w, h = bar.get_width(), bar.get_height()
            if orientation == 'h':
                grad = np.atleast_2d(np.linspace(0, 1 * w / max_value, 256))
            else:
                grad = np.atleast_2d(np.linspace(0, 1 * h / max_value, 256)).T
            norm = cm.colors.NoNorm(vmin=0, vmax=1)
            ax.imshow(grad, extent=[x, x + w, y, y + h], origin='lower', aspect="auto", norm=norm, cmap=my_cmap)

        # draw color bar
        if toggle_color_bar:
            sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=norm)
            sm.set_array([])

            if orientation == 'v' or leaderboard:

                if leaderboard:
                    ax.set_ylabel('')
                    ax.set_xlim(0, max_value)
                else:
                    ax.set_ylim(0, max_value)

                bbox = ax.get_position()
                bottom = bbox.y0
                width = bbox.width * 0.7
                height = bbox.height
                left = bbox.x0 + 0.15 * width

                ax.set_position([left + offset[0], bottom, width, height])
                cbar_ax = ax.figure.add_axes([left - offset[1], bottom, 0.02, height])

                cbar = plt.colorbar(sm, cax=cbar_ax)
                cbar.ax.yaxis.set_label_coords(-0.85, 0.5)
            else:
                ax.set_xlim(0, max_value)
                cbar = plt.colorbar(sm)

            num_ticks = 20
            cbar.ax.yaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
            tick_values = np.linspace(0, max_value, num_ticks - 2)
            tick_labels = ['0.0']
            for x in tick_values:
                x = round(x, 2)
                tick_labels.append(str(x))
            cbar.ax.set_yticklabels(tick_labels)
            cbar.set_label('Proximity to max value found within league', fontsize=7.5)

        return ax

    def draw_ticks_and_labels(self, ax, stat, avg, comparing):
        """
        Function that sets ticks on the graph's axes and prints labels on them. It also prints
        the avg line and faded gray lines for each tick.
        :param ax: current Axes object that allows to access and manipulate the properties of the plot's axes
        :param stat: the statistic that the current graph is plotting.
        :param avg: average value in the league for stat.
        :param comparing: boolean that states wheter the graph being generated is a comparison between players.
        :return: modified Axes object.
        """
        ax.set_xlabel(stat, fontsize=14, fontweight='bold')
        if self.__orientation == 'v':
            ax.set_ylabel('')
            ax.set_yticklabels([])
            tick_values = np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], 18)
            ax.set_yticks(tick_values)
            for y in ax.get_yticks():
                ax.axhline(y=y, linestyle='--', color='gray', alpha=0.2, zorder=-1)

            avg_line_name = self.__position_name + ' \nleague average (' + str("%0.2f" % float(avg)) + ')'
            ax.axhline(avg, color='black', linestyle='-', linewidth=0.7)
            if not comparing:
                ax.text(0.5, avg, avg_line_name, color='black', ha='right', va='center', fontsize=7.6)
            else:
                ax.text(0.5, avg, avg_line_name, color='black', ha='center', va='center', fontsize=7.6)
        else:
            tick_values = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 18)
            ax.set_xticks(tick_values)
            for x in ax.get_xticks():
                ax.axvline(x=x, linestyle='--', color='gray', alpha=0.2, zorder=-1)
            avg_line_name = (self.__position_name.replace(' ', '\n') + ' \nleague \naverage \n' + '(' +
                             str("%0.2f" % float(avg)) + ')')
            ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
            ax.tick_params(axis='x', which='major', labelsize=6)
            ax.axvline(avg, color='black', linestyle='-', linewidth=0.7)
            ax.text(avg, 0.5, avg_line_name, color='black', ha='right', va='center', fontsize=7.6)

    def draw(self, param_map):
        """
        Function that draws a bar plot given a set of parameters.
        :param param_map: set of parameters containing information about the player, the league, and the
        plot's format.
        :return: a bar plot in byte form to be displayed onto a pdf.
        """
        matplotlib.use('agg')
        color_palette = 'Oranges'
        comparing = (self.__compare_name is not None)
        data = param_map.get('league_data')
        stat = param_map.get('stats')
        player_value = (data.loc[data['Player'] == self.__player_name].iloc[0][stat])
        if comparing:
            compare_player_value = data.loc[data['Player'] == self.__compare_name].iloc[0][stat]

        stat_df = data.loc[data['Main position'] == self.__main_pos].loc[:, [stat]]
        stat_list = stat_df[stat].tolist()
        if len(stat_list) != 0:
            avg = sum(stat_list) / len(stat_list)
        else:
            avg = 0

        if not comparing:
            player_data = {' ': [self.__player_name], stat: [player_value]}
        else:
            player_data = {' ': [self.__player_name, self.__compare_name], stat: [player_value, compare_player_value]}

        df = pd.DataFrame(player_data)
        plt.subplot().clear()
        if self.__orientation == 'v':
            sns.barplot(x=" ", y=stat, data=df, orient=self.__orientation)
        else:
            sns.barplot(x=stat, y=" ", data=df, orient=self.__orientation)

        plt.tight_layout()
        ax = plt.gca()
        ax = self.print_value_labels(ax, 12, orientation=self.__orientation)
        ax = self.color_graph(ax, max(stat_df[stat]), color_palette, self.__orientation, [0.06, 0.06])
        ax = self.draw_ticks_and_labels(ax, stat, avg, comparing)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf.getvalue()

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

        for i in range(len(stats)):
            param_map['stats'] = stats[i]
            basic_bar_plots.append(self.draw(param_map))

        return basic_bar_plots
