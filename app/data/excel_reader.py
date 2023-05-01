import pandas as pd


class ExcelReader:
    """
    Class that contains functionality related to reading data from Excel files.
    """

    def read_file(self, file):
        """
        General function for reading data from an Excel (.xlsx) file into a Pandas dataframe.

        :param file: The Excel file containing desired data.
        :return: A Pandas dataframe containing all data in the Excel file, including headers.
        """
        return pd.read_excel(file)

    def player_data(self, player_file):
        """
        Function for extracting the match data of a football player from an Excel file.

        :param player_file: The Excel file containing match data.
        :return: A Pandas dataframe containing all data in the Excel file, including headers.
        """
        return self.read_file(player_file)

    def league_data(self, league_file, player_name):
        """
        Function for extracting the football league data of a single player from an Excel file.

        :param league_file: The Excel file containing league data.
        :param player_name: The name of the player to extract.
        :return: A Pandas dataframe containing all data in the Excel file, including headers.
        :raises KeyError: if the passed player name matches none of the names in the Excel file under the 'Player' col.
        """
        dataframe = self.read_file(league_file)
        try:
            player = dataframe.loc[dataframe['Player'] == player_name]
        except KeyError:
            player = pd.empty()
        return player

    def all_league_data(self, league_file):
        dataframe = self.read_file(league_file)
        return dataframe
