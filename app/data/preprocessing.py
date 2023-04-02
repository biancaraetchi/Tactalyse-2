from .excel_reader import ExcelReader


def get_columns(position):
    """
    Function that provides a list of headers to use for graphing purposes.

    :param position: Position of the player whose stats to graph.
    :return: List of column headers in string form to extract from dataframes when creating PDF graphs.
    """
    return category_dictionary().get(position)


def extract_player(league_df, player_name):
    """
    Function that extracts a single row from a football league dataframe only containing a desired player's data.

    :param league_df:
    :param player_name:
    :return:
    """

    row_df = league_df[league_df['Player'] == player_name]
    return row_df


def position_dictionary():
    """
    Creates a collection of all position codes, with their associated general position.
    Work in progress.

    :return: Dictionary containing all position abbreviations as keys, and the associated general positions as values.
    """

    pos_dict = dict.fromkeys(['RW', 'LW'], 'Winger')
    pos_dict.update(dict.fromkeys(['GK'], 'Goalkeeper'))
    pos_dict.update(dict.fromkeys(['LB', 'RB', 'LWB', 'RWB'], 'Full Back'))
    pos_dict.update(dict.fromkeys(['CB', 'LCB', 'RCB', 'SW'], 'Center Back'))
    pos_dict.update(dict.fromkeys(['DMF'], 'Defensive Midfielder'))
    pos_dict.update(dict.fromkeys(['AMF'], 'Attacking Midfielder'))
    pos_dict.update(dict.fromkeys(['CMF', 'LCMF', 'RCMF'], 'Center Midfielder'))
    pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'Striker'))
    return pos_dict


def category_dictionary():
    """
    Creates a collection of all positions, along with the stats that should be graphed for each position.
    Work in progress.

    :return: Dictionary containing all positions keys, and the associated stats as values.
    """

    cat_dict = dict.fromkeys(['Center Midfielder'], ['Sliding tackles per 90', 'PAdj Sliding tackles',
                                                     'Shots blocked per 90', 'Interceptions per 90',
                                                     'PAdj Interceptions', 'Fouls per 90'])
    return cat_dict


def main_position(player_row):
    """
    Function that

    :param player_row:
    :return:
    """
    player_positions = player_row['Position'].iloc[0]
    first_position = player_positions.split(', ')[0]

    pos_dict = position_dictionary()
    return pos_dict.get(first_position)


def radio_chart_data(league_file, player_name):
    """
    Function that

    :param league_file:
    :param player_name:
    :return:
    """
    reader = ExcelReader()
    league_df = reader.league_data(league_file, player_name)
    player_row = extract_player(league_df, player_name)
    main_pos = main_position(player_row)
    columns = get_columns(main_pos)
    return player_row, columns, main_pos
