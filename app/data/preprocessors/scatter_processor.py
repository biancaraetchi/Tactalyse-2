from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class ScatterProcessor(Preprocessor):
    def get_scatter_columns(self, player_df):
        columns = []
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

    def extract_scatter_data(self, player_file):
        """
        Function that extracts all required data from the passed player data Excel file. Particularly columns that have '/'.
        :param processor: Data preprocessor with general data functions.
        :param player_file: Excel file containing the data of a specific football player.
        :param player_name: The name of the player whose stats to graph.
        :return: Dataframe containing a single row with the player's league data (player_row), columns to use for graphing
                 (columns), main position of the passed player (main_pos_long), and the position abbreviated (main_pos).
        """
        reader = ExcelReader()
        player_df = reader.player_data(player_file)
        scatter_map = {"player_data":player_df}
        columns = self.get_scatter_columns(player_df)
        scatter_map.update({"columns":columns})
        return scatter_map