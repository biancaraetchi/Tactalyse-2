from .pdf_generator import PDFGenerator


class StandardPDF(PDFGenerator):
    def __init__(self):
        super().__init__()

    def print_player_info(self):
        """
        Function that prints player's image and basic information in the first page
        """
        self._pdf.image('app/pdf_generator/resources/images/placeholder_player_photo.jpg', 50, 60, 115)
        self._pdf.set_font(self._pdf.font, 'B', 14)
        self._pdf.print_player_info_col1(self._pdf.player)
        self._pdf.print_player_info_col2(self._pdf.player)

    def generate_pdf(self, param_map):
        """
        Function that generates and returns a pdf based on the data that it receives as parameters
        :param param_map: a map containing key/value pairs for every parameter required to generate the report.
        :return: the generated pdf as a stream output
        """
        league_df = param_map["league_data"]
        player_name = param_map["player_name"]
        main_pos = param_map["main_pos"]
        line_plots = param_map["line_plots"]
        bar_plots = param_map["bar_plots"]

        self._pdf.set_info(player_name, league_df, main_pos)
        self.set_standard_variables(player_name)

        self._pdf.print_title()
        self.print_player_info()

        self.print_plots(line_plots, bar_plots)

        return self._pdf.output(dest='S')
