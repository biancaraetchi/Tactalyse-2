from ..data.preprocessing import extract_league_data
from ..data.preprocessing import extract_player_data
from ..data.preprocessing import extract_all_league_data

def get_all_league_data(league_file):
    return extract_all_league_data(league_file)

def get_league_data(league_file, player_name):
    """
    Function that takes a football league's data along with required parameters, and extracts the relevant data.

    :param league_file: Excel file containing football league data.
    :param player_name: The name of the player whose league data to extract.
    :return: A dataframe containing the player's row of the league file, the columns to be displayed on the chart,
             the player's main position, and an abbreviation of the player's position, in that order.
             (player_row, columns, main_pos_long, main_pos)
    """
    return extract_league_data(league_file, player_name)


def get_player_data(player_file, main_pos):
    """
    Function that takes a football player's match data along with required parameters, and extracts the relevant data.

    :param player_file: Excel file containing a player's match data.
    :param main_pos: The abbreviated position of the player whose league data to extract.
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    return extract_player_data(player_file, main_pos)
