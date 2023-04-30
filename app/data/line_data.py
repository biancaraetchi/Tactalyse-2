from .excel_reader import ExcelReader


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


def extract_line_data(player_file, main_pos):
    """
    Function that extracts all required data from the passed player match data Excel file.

    :param player_file: Excel file containing the match data of a specific football player.
    :param main_pos: The abbreviated general position of the player whose stats to graph.
    :return: DataFrame containing the player's match data (player_df), columns to use for graphing (columns).
    """
    player_df = ExcelReader().player_data(player_file)
    columns = get_columns_line_plots(main_pos)

    return player_df, columns
