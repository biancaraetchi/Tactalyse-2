from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor
import numpy as np


class ScatterProcessor(Preprocessor):
    def get_scatter_columns(self, player_df):
        """
        Function that provides a list of headers to use for graphing the scatter plots.

        :param player_df: player's data frame which will be used for graph.
        :return: All columns containing the required stats to graph.
        """
        columns = []
        if isinstance(player_df, type(None)):
            return columns
        prev = 0
        pairs = 0
        for i in range(len(player_df.columns)):
            if prev==1:
                prev=0
                columns[pairs].append(i)
                pairs=pairs+1
            if "/" in player_df.columns[i]:
                prev=1
                columns.append([])
                columns[pairs].append(i)
        return columns

    def extract_scatter_data(self, player_file, compare_file, player_name, compare_name):
        """
        Function that extracts all required data from the passed player data Excel file. Particularly columns that have '/'.
        :param processor: Data preprocessor with general data functions.
        :param player_file: Excel file containing the data of a specific football player.
        :param player_name: The name of the player whose stats to graph.
        :return: a map with dataframes for the player (`player_data`) and the second player, if any was provided, (`compare_player_data`)
        their names (`player_name` and `compare_player_name`, respectively) and the columns that need to be selected from the dataframe (`columns`,
        in the following format [[x1, y1], [x2, y2], ...]).
        """
        reader = ExcelReader()
        scatter_map = {}
        scatter_map = self.set_player(player_file, player_name, scatter_map, reader)
        scatter_map = self.set_compare_player(compare_file, compare_name, scatter_map, reader)
        scatter_map = self.set_columns(scatter_map)
        return scatter_map
    
    def set_player(self, player_file, player_name, scatter_map, reader):
        """
        Function that sets the player data.

        :param scatter_map: 
        :param player_file: Excel file containing the data of a specific football player.
        :param player_name: The name of the player whose stats to graph.
        :param reader: Excel reader to extract dataframes from Excel files.
        :return: updated scatter_map with a dataframe with all the player data, along with the player name
        """
        player_df = reader.player_data(player_file)
        scatter_map.update({"player_data":player_df})
        scatter_map.update({"player_name":player_name})
        return scatter_map
    
    def set_compare_player(self, compare_file, compare_name, scatter_map, reader):
        """
        Function that sets the compare player data, if it exists.

        :param scatter_map:
        :param compare_file: Excel file containing the data of a specific football player.
        :param compare_name: The name of the player whose stats to graph.
        :param reader: Excel reader to extract dataframes from Excel files.
        :return: updated scatter_map with a dataframe with all the compare player data, along with the compare player name
        """
        if not compare_file:
            return scatter_map
        compare_df = reader.player_data(compare_file)
        scatter_map.update({"compare_player_data":compare_df})
        scatter_map.update({"compare_player_name":compare_name})
        return scatter_map
    
    # def select_only_columns_with_slashes(self, player_df):
    #     """
    #     Function that extracts and sets slashed data in the data frame.

    #     :param scatter_map:
    #     :param player_file: Excel file containing the data of a specific football player.
    #     :return: player dataframe containing only columns that will be extracted for graph generation.
    #     """
    #     columns_to_drop = []
    #     for column in player_df.columns:
    #         if "/" not in column or 'Unnamed' not in column:
    #             columns_to_drop.append(column)
    #     player_df = player_df.drop(columns=columns_to_drop)
    #     return player_df
    
    def set_columns(self, scatter_map):
        """
        Function that sets the param map for drawing scatter plot.

        :param scatter_map:
        :return: scatter_map with updated 'columns' key, containing only columns that will be used for graph generation.
        """
        columns_player = self.get_scatter_columns(scatter_map.get("player_data"))
        if isinstance(scatter_map.get("compare_player_data"), type(None)):
            scatter_map.update({"columns":columns_player})
            return scatter_map
        columns = self.drop_unique_columns(scatter_map.get("player_data"), scatter_map.get("compare_player_data"), columns_player)
        scatter_map.update({"columns":columns})
        return scatter_map
    
    def drop_unique_columns(self, player_df, compare_player_df, columns_player):
        """
        Function that removes unique columns.

        :param player_df: player's data frame which will be used for graph.
        :param compare_player_df: compare player's data frame which will be used for graph.
        :param columns_player: index of columns from the player_df dataframe that will be used for graph generation.
        :return: the indices of the columns with the same data for both player and compare player.
        """
        columns_to_remove = []
        for i in range(len(columns_player)):
            if player_df.columns[columns_player[i][0]] not in compare_player_df.columns:
                columns_to_remove.append(i)
        total_removed = 0
        for i in columns_to_remove:
            del columns_player[i-total_removed]
            total_removed += 1
        return columns_player