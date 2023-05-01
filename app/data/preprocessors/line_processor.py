from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class LineProcessor(Preprocessor):
    def get_columns_line_plots(self, player_pos):
        """
        Function that provides a list of headers to use for graphing the line plots.

        :param player_pos: Abbreviated position of the player whose stats to graph.
        :return: DataFrame containing the required stats to graph.
        """
        stats_file = "app/pdf_generator/resources/test_data/Stats per position.xlsx"
        stats_pd = ExcelReader().read_file(stats_file)
        stats_necessary = stats_pd[['Attribute', player_pos]]
        stats_necessary = stats_necessary[stats_necessary[player_pos] == 1.0]
        return stats_necessary['Attribute']

    def extract_line_data(self, league_file, player_file, player_name, compare_file, compare_name, start_date,
                          end_date):
        """
        Function that extracts all required data from the passed player match data Excel file.

        :param player_file: Excel file containing the match data of a specific football player.
        :return: DataFrame containing the player's match data (player_df), columns to use for graphing (columns).
        """
        reader = ExcelReader()
        player_df = reader.player_data(player_file)
        line_map = {'player_data': player_df}
        league_df = reader.league_data(league_file, player_name)

        player_row = self.extract_player(league_df, player_name)
        main_pos = self.main_position(player_row)
        main_pos_short = self.shortened_dictionary().get(main_pos)
        columns = self.get_columns_line_plots(main_pos_short)
        line_map.update({'columns': columns})

        return line_map
