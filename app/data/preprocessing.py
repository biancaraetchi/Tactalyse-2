import pandas as pd


def get_columns(position):
    """
    Extracts the columns from the 
    """
    return category_dictionary().get(position)


def extract_player(league_df, player_name):
    row_df = league_df[league_df['Player'] == player_name]
    return row_df


def position_dictionary():
    """
    Creates a collection of all position codes, with their associated general position.
    Work in progress.

    Returns:
        dict:Dictionary containing position code strings as keys, and a string representing the general position as
        values.
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
    cat_dict = dict.fromkeys(['Center Midfielder'], ['Sliding tackles per 90', 'PAdj Sliding tackles',
                                                     'Shots blocked per 90', 'Interceptions per 90',
                                                     'PAdj Interceptions', 'Fouls per 90'])
    return cat_dict


def main_position(player_row):
    """
    Returns the general position corresponding to a player's main position in string form.
    """
    player_positions = player_row['Position'].iloc[0]
    first_position = player_positions.split(', ')[0]

    pos_dict = position_dictionary()
    return pos_dict.get(first_position)
