from .excel_reader import ExcelReader


def get_columns_bar_plots(position):
    pass


def extract_bar_data(league_file):
    reader = ExcelReader()
    league_df = reader.all_league_data(league_file)
    return league_df
