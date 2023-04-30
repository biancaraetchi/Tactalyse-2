from .excel_reader import ExcelReader


def get_columns_radar_chart(processor, position):
    """
    Function that provides a list of headers to use for graphing the radio chart.

    :param processor: Data preprocessor with general data functions.
    :param position: Full position name of the player whose stats to graph.
    :return: List of column headers in string form to extract from dataframes when creating PDF graphs.
    """
    return processor.league_category_dictionary().get(position)


def extract_radar_data(processor, league_file, player_name):
    """
    Function that extracts all required data from the passed league data Excel file.

    :param processor: Data preprocessor with general data functions.
    :param league_file: Excel file containing the data of a specific football league.
    :param player_name: The name of the player whose stats to graph.
    :return: Dataframe containing a single row with the player's league data (player_row), columns to use for graphing
             (columns), main position of the passed player (main_pos_long), and the position abbreviated (main_pos).
    """
    reader = ExcelReader()
    league_df = reader.league_data(league_file, player_name)
    player_row = processor.extract_player(league_df, player_name)
    main_pos = processor.main_position(player_row)

    main_pos_long = processor.position_dictionary().get(main_pos)
    main_pos = processor.shortened_dictionary().get(main_pos)
    columns = get_columns_radar_chart(processor, main_pos)

    return player_row, columns, main_pos_long, main_pos
