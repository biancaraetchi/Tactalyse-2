import io

import matplotlib.pyplot as plt
import seaborn as sns

from .bar_plot import BarPlot


class LeaderboardBarPlot(BarPlot):
    """
    A class representing a horizontal bar plot where the player's statistic is shown amongst
    the other players' values in a leaderboard format, displaying the player's ranking. 
    """

    def __init__(self, param_map):
        super().__init__(param_map)
        self.__position_name = param_map.get('player_pos')
        self.__player_name = param_map.get('player_name')
        self.__compare_name = param_map.get('compare_name')
        self.__compare_pos = param_map.get('compare_pos')

    def draw_ticks_and_labels(self, ax, data, compared_player, ranking):
        """
        :return: modified Axes object.
        """
        new_labels = []
        for string in data['Player']:
            if (string != self.__player_name and not compared_player) or (
                    string != self.__compare_name and compared_player):
                new_string = string
            else:
                new_string = string + '\n(' + str(ranking) + 'th)'
            new_labels.append(new_string)

        plt.yticks(range(len(data.iloc[:, 1])), new_labels)
        plt.yticks(fontsize=9)
        labels = ax.get_yticklabels()
        labels[5].set_fontsize(11)
        labels[5].set_weight('bold')
        plt.xticks(fontsize=12)
        ax.xaxis.get_label().set_size(14)

        return ax

    def draw_leaderboard(self, param_map, compared_player=False):
        """
        Function that draws a leaderboard bar graph showing the player's ranking for a given statistic,
        found in param_map.
        The graph shows the 5 players above and below the analysed one and provides the main player's
        ranking.
        Since values between adjacent rankings may not differ a lot, the graph is "zoomed in"
        by a factor set by zoom_values.
        :param compared_player: is True if the graph being generated is about the compared player 
        and not the main one. 
        :param param_map: a dictionary containing information about the player(s) and their league.
        :return: a leaderboard bar plot in byte form.
        """
        color_palette = 'Oranges'
        zoom_values = [5 / 6, 6 / 5]

        stat = param_map.get('stats')
        data = param_map.get('league_data')
        data = data.sort_values(by=stat, ascending=False)
        data = data.reset_index()
        max_value = max(data[stat])

        if not compared_player:
            ranking = self.get_index(data, self.__player_name)
        else:
            ranking = self.get_index(data, self.__compare_name)

        for i in range(len(data)):
            if i < ranking - 5 or i > ranking + 5:
                data.drop(index=i, inplace=True)

        plt.subplot().clear()
        sns.barplot(x=stat, y='Player', data=data, linewidth=0.0001)
        plt.xlim([0, max(data[stat]) + 1])
        plt.tight_layout()

        ax = plt.gca()
        ax = self.draw_ticks_and_labels(ax, data=data, compared_player=compared_player, ranking=ranking)
        ax = self.print_value_labels(ax, 8, 'h')
        ax = self.color_graph(ax, max_value, color_palette, 'h', [0.13, 0.13], leaderboard=True)

        start = zoom_values[0] * min(data[stat])
        end = zoom_values[1] * max(data[stat])
        ax.set_xlim(start, end)
        for x in ax.get_xticks():
            ax.axvline(x=x, linestyle='--', color='gray', alpha=0.5, zorder=-1)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf.getvalue()

    def draw_all(self, param_map):
        """
        Function that draws leaderboard plots for each of the player's best statistics.
        :param param_map: a dictionary containing information about the player and their league.
        :return: a list of leaderboard bar plots in byte form.
        """
        comparable = self.are_comparable(self.__compare_name, self.__position_name, self.__compare_pos)
        if comparable:
            stats = param_map.get('stats')
        else:
            stats = self.get_stats_superset()

        leaderboard_bar_plots = []
        best_stats_list = self.get_best_stats(param_map, self.__player_name, stats)
        for stat in best_stats_list:
            param_map['stats'] = stat
            leaderboard_bar_plots.append(self.draw_leaderboard(param_map))

        # In case of a comparison with another player, draw leaderboards for their best stats too.
        if self.__compare_name is not None:
            print('COMPARING')
            best_stats_list = self.get_best_stats(param_map, self.__compare_name, stats)
            for stat in best_stats_list:
                param_map['stats'] = stat
                leaderboard_bar_plots.append(self.draw_leaderboard(param_map, True))

        return leaderboard_bar_plots
