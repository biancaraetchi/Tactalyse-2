from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class BarProcessor(Preprocessor):
    def get_columns_bar_plots(self, position):
        """
        Function that provides a list of headers to use for graphing the bar plots.

        :param position: Abbreviated position of the player whose stats to graph.
        :return: DataFrame containing the required stats to graph.
        """
        short_position = self.shortened_dictionary().get(position)
        return self.league_category_dictionary().get(short_position)

    def extract_bar_data(self, league_file, player_name, compare_name):
        """
        Function that extracts all required data from the passed player match data Excel file.

        :param param_map:
        :return: DataFrame containing the player's match data (player_df), columns to use for graphing (columns).
        """
        reader = ExcelReader()
        league_df = reader.all_league_data(league_file)
        bar_map = {"league_data": league_df}
        player_row = reader.league_data(league_file, player_name, compare_name)
        main_pos = self.main_position(player_row.loc[player_row['Player'] == player_name])
        bar_map.update({"main_pos": main_pos})
        player_pos = self.position_dictionary().get(main_pos)
        bar_map.update({"player_pos": player_pos})
        stats = self.get_columns_bar_plots(main_pos)
        bar_map.update({"stats": stats})
        bar_map.update({"player_name": player_name})

        if compare_name == None:
            bar_map.update({"compare_name": None})
        else:
            compare_row = player_row.loc[player_row['Player'] == compare_name] 
            compare_pos = self.position_dictionary().get(self.main_position(compare_row))
            bar_map.update({"compare_name": compare_name})
            bar_map.update({"compare_pos": compare_pos})

        return bar_map
