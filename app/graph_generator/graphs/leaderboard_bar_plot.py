from .main_stats_bar_plot import *

class LeaderboardBarPlot(MainStatsBarPlot):

    def __init__(self, param_map):
        param_map.update({"orientation": 'v'})
        super().__init__(param_map)
        self.__position_name = param_map.get('player_pos')
        self.__main_pos = param_map.get('main_pos')
        self.__player_name = param_map.get('player_name')
        self.__compare_name = param_map.get('compare_name')
        self.__compare_pos = param_map.get('compare_pos')
    
    def draw(self, param_map, compared_player = False):

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

