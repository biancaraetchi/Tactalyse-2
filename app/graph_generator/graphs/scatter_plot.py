import io

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .abstract_models import Graph


class ScatterPlot(Graph):
    """
    Class to generate a scatter plot.
    """

    def __init__(self):
        """
        Function that initializes an instance of the scatter plot class.
        """
        pass

    def draw(self, param_map):
        """
        Function that draws a scatter plot based on the data inside `param_map`.
        :param param_map: a map with dataframes for the player (`player_data`) and the second player, if any was provided, (`compare_player_data`)
        their names (`player_name` and `compare_player_name`, respectively) and the columns that need to be selected from the dataframe (`columns`,
        in the following format: [x1, y1]).
        :return: a scatter plot representing the data in `param_map`.
        """
        column_numbers = param_map.get('columns')
        data = param_map.get('player_data')
        fig, ax = plt.subplots()
        ax.clear()
        #axis_titles needs to be split on the '/', since the data columns are formatted in the following manner: "Total goals / successful",
        #where "Total goals" and "successful" will represent different axis names
        axis_titles=data.columns[column_numbers[0]].split("/")
        compare_data = param_map.get("compare_player_data")
        if isinstance(compare_data, type(None)):
            #if there is no second player, create a map with the data from the 'player_data' dataframe.
            enter_data={axis_titles[0]:data[data.columns[column_numbers[0]]], axis_titles[1]:data[data.columns[column_numbers[1]]]}
            hue = None
        else:
            #if there is a second player, add a column to the dataframes, each representing the name of the respective player (for plot legend purposes)
            data["Player"] = [param_map.get('player_name')] * len(data)
            compare_data["Player"] = [param_map.get('compare_player_name')] * len(compare_data)
            #combine the columns from the two dataframes into one
            necessary_data = pd.concat([data, compare_data])
            #create a map with the new data, and add the "Player" column in there as well.
            enter_data={axis_titles[0]:necessary_data[data.columns[column_numbers[0]]], axis_titles[1]:necessary_data[data.columns[column_numbers[1]]], "Player":necessary_data['Player']}
            hue = "Player"
        enter_data=pd.DataFrame(data=enter_data)
        sns.lmplot(x=axis_titles[0], y=axis_titles[1],data=enter_data, hue=hue)

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return buffer.getvalue()
    
    def draw_all(self, param_map):
        """
        Function that draws scatter plots for all columns inside `param_map`.
        :param param_map: a map with dataframes for the player (`player_data`) and the second player, if any was provided, (`compare_player_data`)
        their names (`player_name` and `compare_player_name`, respectively) and the columns that need to be selected from the dataframe (`columns`,
        in the following format [[x1, y1], [x2, y2], ...]).
        :return: an array of scatter plots representing the data in `param_map`.
        """
        columns = param_map.get('columns')
        plots = []
        for column in columns:
            #rewrite the `columns` variable to represent a single pair of columns at a time (ease of use in next function).
            param_map['columns'] = column
            plots.append(self.draw(param_map))
        return plots
