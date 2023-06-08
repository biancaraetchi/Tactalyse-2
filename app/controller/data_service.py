from app.data.preprocessors.bar_processor import BarProcessor
from app.data.preprocessors.line_processor import LineProcessor
from app.data.preprocessors.pdf_processor import PDFProcessor
from app.data.preprocessors.preprocessor import Preprocessor
from app.data.preprocessors.radar_processor import RadarProcessor
from app.data.preprocessors.scatter_processor import ScatterProcessor


class DataService:
    def get_bar_data(self, league_file, player_name, compare_name):
        """
        Function that takes a football league's data along with required parameters, and extracts the relevant data for a
        bar chart.

        :param league_file: Excel file containing football league data.
        :param player_name: The name of the player whose league data to extract.
        :param compare_name: The name of the player to compare with and whose league data to extract.
        :return: A parameter map containing processed data needed for bar graph generation.
        """
        processor = BarProcessor()
        return processor.extract_bar_data(league_file, player_name, compare_name)

    def get_radar_data(self, league_file, player_name, compare_name):
        """
        Function that takes a football league's data along with required parameters, and extracts the relevant data for a
        radar chart.

        :param league_file: Excel file containing football league data.
        :param player_name: The name of the player whose league data to extract.
        :param compare_name: The name of the player to compare with and whose league data to extract.
        :return: A parameter map containing processed data needed for radar graph generation.
        """
        processor = RadarProcessor()
        return processor.extract_radar_data(league_file, player_name, compare_name)

    def get_line_data(self, league_file, player_file, player_name, compare_file, compare_name, start_date, end_date):
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
        :return: A parameter map containing processed data needed for line graph generation.
        """
        processor = LineProcessor()
        return processor.extract_line_data(league_file, player_file, player_name, compare_file, compare_name,
                                           start_date,
                                           end_date)

    def get_scatter_data(self, player_file, compare_file, player_name, compare_name):
        """
        Function that takes a football player's data along with required parameters, and extracts the relevant data for a
        scatter plot.
        :param player_file: Excel file containing a player's match data.
        :param compare_file: Excel file containing a second players' match data, or None, if there is no comparison.
        :param player_name: The abbreviated name of the player, in the format of "J. Doe".
        :param compare_name: The abbreviated name of the second player, if any is provided, in the format of "J. Doe".
        :return: A parameter map containing processed data needed for scatter plot generation.
        """
        processor = ScatterProcessor()
        return processor.extract_scatter_data(player_file, compare_file, player_name, compare_name)

    def get_pdf_data(self, league_data, player_name, league_name, compare_name, line_plots, bar_plots,
                     player_image=None, player_cmp_image=None):
        """
        Function that takes a football player's data along with required parameters, and extracts the relevant data for a
        pdf.

        :param league_data: Excel file containing the data of a specific football league.
        :param player_name: The name of the player whose data to extract.
        :param league_name: Name of the player to compare to in the report.
        :param compare_name: The name of the player to compare with and whose data to extract.
        :param line_plots:
        :param bar_plots:
        :param player_image: Image representing the main player.
        :param player_cmp_image: Image representing the compare player.
        :return: A parameter map containing processed data needed for PDF generation.
        """
        processor = PDFProcessor()
        return processor.params_to_map(league_data, player_name, league_name,
                                       compare_name, line_plots, bar_plots, player_image, player_cmp_image)

    def both_in_league(self, league_file, player_name, compare_name):
        """
        Function that checks if the player and the player to compare to are both included in the same league file

        :param league_file: Excel file containing league data
        :param player_name: Name of the main player
        :param compare_name: Name of the comparison player
        :return: True if they're both in the league file, false if not
        """
        processor = Preprocessor()
        if processor.in_league(league_file, player_name) and processor.in_league(league_file, compare_name):
            return True
        else:
            return False
