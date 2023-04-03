from .excel_reader import league_data
from .excel_reader import player_data
from .excel_reader import ExcelReader

#THERE IS NO DATA FOR CENTER MIDFIELDER IN STATS PER POSITION
#I MADE UP SOME DATA, BUT IT'S NOT ACCURATE

def get_columns_polar_chart(position):
    """
    Extracts the columns from the 
    """
    return category_dictionary().get(position)

def get_columns_line_plots(player_pos):
    stats_file = "app/pdf_generator/resources/test_data/Stats per position.xlsx"
    stats_pd = ExcelReader().read_file(stats_file)
    stats_necessary = stats_pd[['Attribute',player_pos]]
    stats_necessary = stats_necessary[stats_necessary[player_pos] == 1.0]
    return stats_necessary['Attribute']


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

def shortened_dictionary():
    pos_dict = dict.fromkeys(['RW', 'LW'], 'WI')
    pos_dict.update(dict.fromkeys(['GK'], 'GK'))
    pos_dict.update(dict.fromkeys(['LB', 'RB', 'LWB', 'RWB'], 'FB'))
    pos_dict.update(dict.fromkeys(['CB', 'LCB', 'RCB', 'SW'], 'CB'))
    pos_dict.update(dict.fromkeys(['DMF'], 'DM'))
    pos_dict.update(dict.fromkeys(['AMF'], 'AM'))
    pos_dict.update(dict.fromkeys(['CMF', 'LCMF', 'RCMF'], 'CM'))
    pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'ST'))
    
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
    # print(first_position)
    # pos_dict = position_dictionary()
    return first_position


def radio_chart_data(league_file, player_name):
    league_df = league_data(league_file, player_name)
    player_row = extract_player(league_df, player_name)
    main_pos = main_position(player_row)
    main_pos_long = position_dictionary().get(main_pos)
    columns = get_columns_polar_chart(main_pos_long)
    return player_row, columns, main_pos_long, main_pos

def line_plot_data(player_file, main_pos):
    player_df = player_data(player_file)
    main_pos_short = shortened_dictionary().get(main_pos)
    columns = get_columns_line_plots(main_pos_short)

    return player_df, columns
