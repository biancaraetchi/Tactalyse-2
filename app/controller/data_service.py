from ..data.excel_reader import ExcelReader
from ..data.preprocessing import get_columns, main_position


def read_files_standard(league_file, player_file):
    reader = ExcelReader()
    league_df = reader.read_file(league_file)
    player_df = reader.read_file(player_file)
    return league_df, player_df


def get_main_position(league_df, player_name):
    player_positions = league_df.loc[league_df['Player'] == player_name]['Position'].iloc[0]
    first_position = player_positions.split(', ')[0]
    return main_position(first_position)


def get_column_names(dataframe):
    return get_columns(dataframe, None)
