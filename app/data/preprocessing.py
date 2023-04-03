from .excel_reader import ExcelReader


def get_columns_radio_chart(position):
    """
    Function that provides a list of headers to use for graphing the radio chart.

    :param position: Full position name of the player whose stats to graph.
    :return: List of column headers in string form to extract from dataframes when creating PDF graphs.
    """
    return league_category_dictionary().get(position)


def get_columns_line_plots(player_pos):
    """
    Function that provides a list of headers to use for graphing the line plots.

    :param player_pos: Abbreviated position of the player whose stats to graph.
    :return: DataFrame containing the required stats to graph.
    """
    stats_file = "app/pdf_generator/resources/test_data/Stats per position.xlsx"
    stats_pd = ExcelReader().read_file(stats_file)
    stats_necessary = stats_pd[['Attribute', player_pos]]
    stats_necessary = stats_necessary[stats_necessary[player_pos] == 1.0]
    return stats_necessary['Attribute']


def extract_player(league_df, player_name):
    """
    Function that extracts a single row from a football league dataframe only containing a desired player's data.

    :param league_df: Dataframe containing league data of football players.
    :param player_name: Name of the player whose data to extract.
    :return: A DataFrame containing a single row with the data of the specified player.
    """

    row_df = league_df[league_df['Player'] == player_name]
    return row_df


def position_dictionary():
    """
    Creates a collection of all position codes, with their associated general position in full words.
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


def shortened_dictionary():
    """
    Creates a collection of all position codes, with their associated general position as abbreviations.
    Work in progress.

    :return: Dictionary containing all position abbreviations as keys, and the associated general position abbreviations
             as values.
    """
    pos_dict = dict.fromkeys(['RW', 'LW'], 'WI')
    pos_dict.update(dict.fromkeys(['GK'], 'GK'))
    pos_dict.update(dict.fromkeys(['LB', 'RB', 'LWB', 'RWB'], 'FB'))
    pos_dict.update(dict.fromkeys(['CB', 'LCB', 'RCB', 'SW'], 'CB'))
    pos_dict.update(dict.fromkeys(['DMF'], 'DM'))
    pos_dict.update(dict.fromkeys(['AMF'], 'AM'))
    pos_dict.update(dict.fromkeys(['CMF', 'LCMF', 'RCMF'], 'CM'))
    pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'ST'))

    return pos_dict


def league_category_dictionary():
    """
    Creates a collection of all positions, along with the league stats that should be graphed in the radio chart for
    each position.
    Work in progress.

    :return: Dictionary containing all positions as keys, and the associated stats as values.
    """

    cat_dict = dict.fromkeys(['Center Midfielder'], ['Sliding tackles per 90', 'PAdj Sliding tackles',
                                                     'Shots blocked per 90', 'Interceptions per 90',
                                                     'PAdj Interceptions', 'Fouls per 90'])
    return cat_dict


def main_position(player_row):
    """
    Function that retrieves the main position of a football player.

    :param player_row: Dataframe containing the league data of a single player.
    :return: The first position in the list of player positions.
    """
    player_positions = player_row['Position'].iloc[0]
    first_position = player_positions.split(', ')[0]
    return first_position


def extract_league_data(league_file, player_name):
    """
    Function that extracts all required data from the passed league data Excel file.

    :param league_file: Excel file containing the data of a specific football league.
    :param player_name: The name of the player whose stats to graph.
    :return: Dataframe containing a single row with the player's league data (player_row), columns to use for graphing
             (columns), main position of the passed player (main_pos_long), and the position abbreviated (main_pos).
    """
    reader = ExcelReader()
    league_df = reader.league_data(league_file, player_name)
    player_row = extract_player(league_df, player_name)
    main_pos = main_position(player_row)
    main_pos_long = position_dictionary().get(main_pos)
    main_pos = shortened_dictionary().get(main_pos)
    columns = get_columns_radio_chart(main_pos_long)
    return player_row, columns, main_pos_long, main_pos


def extract_player_data(player_file, main_pos):
    """
    Function that extracts all required data from the passed player match data Excel file.

    :param player_file: Excel file containing the match data of a specific football player.
    :param main_pos: The abbreviated general position of the player whose stats to graph.
    :return: DataFrame containing the player's match data (player_df), columns to use for graphing (columns).
    """
    player_df = ExcelReader().player_data(player_file)
    columns = get_columns_line_plots(main_pos)

    return player_df, columns
