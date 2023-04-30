from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class BarProcessor(Preprocessor):
    def get_columns_bar_plots(self, position):
        preproc = Preprocessor()
        short_position = preproc.shortened_dictionary().get(position)
        return preproc.league_category_dictionary().get(short_position)


    def extract_bar_data(self, league_file, player_name):
        reader = ExcelReader()
        league_df = reader.all_league_data(league_file)
        bar_map = {"league_data": league_df}
        player_row = reader.league_data(league_file, player_name)
        main_pos = self.main_position(player_row)
        bar_map.update({"main_pos": main_pos})
        player_pos = self.position_dictionary().get(main_pos)
        bar_map.update({"player_pos": player_pos})
        stats = self.get_columns_bar_plots(main_pos)
        bar_map.update({"stats": stats})
        bar_map.update({"player_name": player_name})
        return bar_map