from .preprocessor import Preprocessor
from ..excel_reader import ExcelReader


class LineProcessor(Preprocessor):
    def __init__(self):
        self.__reader = ExcelReader()

    def get_columns_line_plots(self, player_pos):
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

    def extract_line_data(self, league_file, player_file, player_name, compare_file, compare_name, start_date,
                          end_date):
        """
        Function that extracts all required data from the passed player match data Excel file.

        :param league_file:
        :param player_file:
        :param player_name:
        :param compare_file:
        :param compare_name:
        :param start_date:
        :param end_date:
        :return: Map containing data required for generating a bar plot.
        """
        line_map = {'type': "line"}

        line_map = self.set_player(player_name, line_map)
        line_map = self.set_compare(compare_name, compare_file, line_map)
        line_map = self.set_player_data(player_name, player_file, league_file, line_map)
        line_map = self.set_tactalyse_data(start_date, end_date, line_map)
        line_map = self.set_stats(line_map.get('main_pos_short'), line_map)

        return line_map

    def set_player(self, player_name, line_map):
        """
        Function that sets the player name.

        :param player_name:
        :param line_map:
        :return: Passed line_map with the player appended for key 'player'.
        """
        line_map.update({'player': player_name})
        return line_map

    def set_compare(self, compare, compare_file, line_map):
        """
        Function that sets the compare player's name and data.

        :param compare:
        :param compare_file:
        :param line_map:
        :return: Passed line_map with the compare player appended for key 'compare', and their match data for key
        'compare_data'.
        """
        if not compare:
            return line_map
        line_map.update({'compare': compare})

        compare_df = self.__reader.player_data(compare_file)
        line_map.update({'compare_data': compare_df})
        return line_map

    def set_player_data(self, player_name, player_file, league_file, line_map):
        """
        Function that sets the player's positional information and data

        :param player_name:
        :param player_file:
        :param league_file:
        :param line_map:
        :return: Passed line_map with the player's position appended in different formats, and their match data.
        """
        player_df = self.__reader.player_data(player_file)
        line_map.update({'player_data': player_df})

        player_row = self.__reader.league_data(league_file, player_name)
        main_pos = self.main_position(player_row)
        line_map.update({'main_pos': main_pos})

        player_pos = self.position_dictionary().get(main_pos)
        line_map.update({'player_pos': player_pos})

        main_pos_short = self.shortened_dictionary().get(main_pos)
        line_map.update({'main_pos_short': main_pos_short})
        return line_map

    def set_tactalyse_data(self, start_date, end_date, line_map):
        """
        Function that sets the player's start and end date of Tactalyse's contract with them.

        :param start_date:
        :param end_date:
        :param line_map:
        :return: Passed line_map with the start and end date appended.
        """
        line_map.update({'start_date': start_date})
        line_map.update({'end_date': end_date})
        return line_map

    def set_stats(self, player_pos, line_map):
        """
        Function that sets the columns to use in graphing for the player position.

        :param player_pos:
        :param line_map:
        :return: Passed line_map with the columns appended as a list for header 'columns'.
        """
        columns = self.get_columns_line_plots(player_pos)
        line_map.update({'columns': columns})
        return line_map
