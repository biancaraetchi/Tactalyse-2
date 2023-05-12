from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class RadarProcessor(Preprocessor):
    def get_columns_radar_chart(self, position):
        """
        Function that provides a list of headers to use for graphing the radio chart.

        :param processor: Data preprocessor with general data functions.
        :param position: Full position name of the player whose stats to graph.
        :return: List of column headers in string form to extract from dataframes when creating PDF graphs.
        """
        return self.league_category_dictionary().get(position)

    def extract_radar_data(self, league_file, player_name, compare_name):
        """
        Function that extracts all required data from the passed league data Excel file.

        :param processor: Data preprocessor with general data functions.
        :param league_file: Excel file containing the data of a specific football league.
        :param player_name: The name of the player whose stats to graph.
        :param compare_name: The name of the player to compare with and whose league data to extract.
        :return: Dataframe containing a single row with the player's league data (player_row), columns to use for graphing
                 (columns), main position of the passed player (main_pos_long), and the position abbreviated (main_pos).
        """
        reader = ExcelReader()
        league_df = reader.league_data(league_file, player_name, compare_name)

        player_row = self.extract_player(league_df, player_name)
        radar_map = {'player_row': player_row}

        main_pos = self.main_position(player_row)
        main_pos_long = self.position_dictionary().get(main_pos)
        radar_map.update({'main_pos_long': main_pos_long})
        main_pos = self.shortened_dictionary().get(main_pos)
        radar_map.update({'main_pos': main_pos})

        columns = self.get_columns_radar_chart(main_pos)
        radar_map.update({'columns': columns})

        return radar_map
