from ..data.excel_reader import ExcelReader
from ..data.preprocessing import get_columns, main_position
from ..data.preprocessing import extract_player


def read_files_standard(league_file, player_file):
    reader = ExcelReader()
    league_df = reader.read_file(league_file)
    player_df = reader.read_file(player_file)
    return league_df, player_df


def get_player_row(league_df, player_name):
    return extract_player(league_df, player_name)


def get_main_position(player_row):
    return main_position(player_row)


def get_column_names(player_pos):
    return get_columns(player_pos)
