from ..data.line_data import extract_line_data
from ..data.radar_data import extract_radar_data
from ..data.bar_data import extract_bar_data
from ..data.scatter_data import extract_scatter_data


def get_bar_data(league_file):
    return extract_bar_data(league_file)


def get_radar_data(processor, league_file, player_name):
    """
    Function that takes a football league's data along with required parameters, and extracts the relevant data for a
    radar chart.

    :param processor: Data preprocessor with general data functions.
    :param league_file: Excel file containing football league data.
    :param player_name: The name of the player whose league data to extract.
    :return: A dataframe containing the player's row of the league file, the columns to be displayed on the chart,
             the player's main position, and an abbreviation of the player's position, in that order.
             (player_row, columns, main_pos_long, main_pos)
    """
    return extract_radar_data(processor, league_file, player_name)


def get_line_data(player_file, main_pos):
    """
    Function that takes a football player's data along with required parameters, and extracts the relevant data for a
    line plot.

    :param player_file: Excel file containing a player's match data.
    :param main_pos: The abbreviated position of the player whose league data to extract.
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    return extract_line_data(player_file, main_pos)

def get_scatter_data(processor, player_file, player_name):
    """
    Function that takes a football player's data along with required parameters, and extracts the relevant data for a
    line plot.

    :param player_file: Excel file containing a player's match data.
    :param main_pos: The abbreviated position of the player whose league data to extract.
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    return extract_scatter_data(processor, player_file, player_name)
