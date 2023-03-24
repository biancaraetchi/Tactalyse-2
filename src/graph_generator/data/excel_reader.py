import pandas as pd


def player_data(player_file):
    """
    Returns a dataframe representing the passed player data excel file
    """

    data = pd.read_csv(player_file, header=0, names=0)
    return data


def league_data(league_file, player_name):
    """
    Returns a dataframe representing the passed player data excel file
    """

    dataframe = pd.read_csv(league_file, header=0, names=0)
    try:
        player = dataframe.loc[dataframe['Player'] == player_name]
    except KeyError:
        player = pd.empty()
    return player
