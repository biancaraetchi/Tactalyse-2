import pandas as pd

class ExcelReader:
    def read_file(file):
        return pd.read_csv(file, header=0, names=0)

def player_data(player_file):
    """
    Returns a dataframe representing the passed player data excel file
    """
    data = ExcelReader().read_file(player_file)
    return data


def league_data(league_file, player_name):
    """
    Returns a dataframe representing the league data of a passed player
    """
    dataframe = ExcelReader().read_file(league_file)
    try:
        player = dataframe.loc[dataframe['Player'] == player_name]
    except KeyError:
        player = pd.empty()
    return player
