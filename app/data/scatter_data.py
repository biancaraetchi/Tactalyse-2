from .excel_reader import ExcelReader

def extract_scatter_data(processor, player_file, player_name):
    """
    Function that extracts all required data from the passed league data Excel file.

    :param processor: Data preprocessor with general data functions.
    :param player_file: Excel file containing the data of a specific football player.
    :param player_name: The name of the player whose stats to graph.
    :return: Dataframe containing a single row with the player's league data (player_row), columns to use for graphing
             (columns), main position of the passed player (main_pos_long), and the position abbreviated (main_pos).
    """
    reader = ExcelReader()
    league_df = reader.league_data(player_file, player_name)
    player_row = processor.extract_player(league_df, player_name)
    main_pos = processor.main_position(player_row)

    main_pos_long = processor.position_dictionary().get(main_pos)
    main_pos = processor.shortened_dictionary().get(main_pos)

    return player_row, main_pos_long, main_pos