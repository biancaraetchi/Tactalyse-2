from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class BarProcessor(Preprocessor):
    def get_columns_bar_plots(self, position):
        return ['Goals']

    def extract_bar_data(self, league_file, player_name):
        reader = ExcelReader()
        league_df = reader.all_league_data(league_file)
        bar_map = {"league_data": league_df}
        player_row = reader.league_data(league_file, player_name)
        main_pos = self.main_position(player_row)
        player_pos = self.position_dictionary().get(main_pos)
        bar_map.update({"player_pos": player_pos})
        stats = self.get_columns_bar_plots(player_pos)
        bar_map.update({"stats": stats})
        bar_map.update({"player_name": player_name})
        return bar_map
