from ..data.preprocessing import radio_chart_data


def get_radio_chart_data(league_file, player_name):
    """
    Function that passes raw data structures containing data relevant to the radio chart, and extracts the relevant
    data.

    :param league_file: Excel file containing football league data.
    :param player_name: The name of the player whose league data to extract.
    :return: A dataframe containing the player's row of the league file, the columns to be displayed on the chart,
             and the player's main position, in that order. (player_row, columns, main_pos)
    """
    return radio_chart_data(league_file, player_name)
