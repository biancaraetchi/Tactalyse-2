from app.data.preprocessors.line_processor import LineProcessor
from app.data.preprocessors.radar_processor import RadarProcessor
from app.data.preprocessors.bar_processor import BarProcessor
from app.data.preprocessors.pdf_processor import PDFProcessor
from app.data.preprocessors.preprocessor import Preprocessor
from app.data.preprocessors.scatter_processor import ScatterProcessor


def get_bar_data(league_file, player_name):
    processor = BarProcessor()
    return processor.extract_bar_data(league_file, player_name)


def get_radar_data(league_file, player_name, compare_name):
    """
    Function that takes a football league's data along with required parameters, and extracts the relevant data for a
    radar chart.

    :param league_file: Excel file containing football league data.
    :param player_name: The name of the player whose league data to extract.
    :param compare_name: The name of the player to compare with and whose league data to extract.
    :return: A dataframe containing the player's row of the league file, the columns to be displayed on the chart,
             the player's main position, and an abbreviation of the player's position, in that order.
             (player_row, columns, main_pos_long, main_pos)
    """
    processor = RadarProcessor()
    return processor.extract_radar_data(league_file, player_name, compare_name)


def get_line_data(league_file, player_file, player_name, compare_file, compare_name, start_date, end_date):
    """
    Function that takes a football player's data along with required parameters, and extracts the relevant data for a
    line plot.

    :param league_file: Excel file containing the data of a specific football league.
    :param player_file: Excel file containing a player's match data.
    :param player_name: The name of the player whose data to extract.
    :param compare_file: Excel file containing match data of the player to compare with.
    :param compare_name: The name of the player to compare with and whose data to extract.
    :param start_date: Start date of Tactalyse's services for the main player.
    :param end_date: End date of Tactalyse's services for the main player.
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    processor = LineProcessor()
    return processor.extract_line_data(league_file, player_file, player_name, compare_file, compare_name, start_date, end_date)


def get_scatter_data(player_file, player_name):
    """
    Function that takes a football player's data along with required parameters, and extracts the relevant data for a
    line plot.
    :param player_file: Excel file containing a player's match data.
    :param player_name: The abbreviated position of the player whose league data to extract.
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    processor = ScatterProcessor
    return processor.extract_scatter_data(player_file, player_name)


def get_pdf_data(league_data, player_name, compare_name, line_plots, bar_plots, scatter_plots):
    """
    Function that takes a football player's data along with required parameters, and extracts the relevant data for a
    pdf.

    :param league_data: Excel file containing the data of a specific football league.
    :param player_name: The name of the player whose data to extract.
    :param compare_name: The name of the player to compare with and whose data to extract.
    :param line_plots:
    :param bar_plots:
    :param scatter_plots:
    :return: A dataframe containing the player's match data, and the columns to be displayed on the line plots, in that
             order. (player_data, columns_line_plot)
    """
    processor = PDFProcessor()
    return processor.params_to_map(league_data, player_name, compare_name, line_plots, bar_plots, scatter_plots)


def both_in_league(league_file, player_name, compare_name):
    """
    Function that checks if the player and the player to compare to are both included in the same league file

    :param league_file:
    :param player_name:
    :param compare_name:
    :return: True if they're both in the league file, false if not
    """
    processor = Preprocessor()
    if processor.in_league(league_file, player_name) and processor.in_league(league_file, compare_name):
        return True
    else:
        return False
