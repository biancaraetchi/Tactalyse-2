from .pdf_generator import PDFGenerator


class ComparisonPDF(PDFGenerator):
    def print_player_info(self):
        """
        Function that prints player's and compare player's image and basic information in the first page
        """
        self._pdf.image('app/pdf_generator/resources/images/placeholder_player_photo.jpg', 10, 60, 60, 60)
        self._pdf.image('app/pdf_generator/resources/images/Foto william Troost-Ekong.jpeg', 10, 140, 60, 60)
        self._pdf.set_font(self._pdf.font, 'B', 14)
        self._pdf.print_comparison_info_col1(self._pdf.player, self._pdf.compare)
        # self._pdf.print_comparison_info_col2(self._pdf.player, self._pdf.compare)
        

    def generate_pdf(self, param_map):
        """
        Function that generates and returns a pdf based on the data that it receives as parameters
        :param param_map: a map containing key/value pairs for every parameter required to generate the report.
        :return: the generated pdf as a stream output
        """
        league_df = param_map["league_data"]
        player_name = param_map["player_name"]
        main_pos = param_map["main_pos"]
        compare_name = param_map["compare_name"]
        compare_pos = param_map["compare_pos"]
        line_plots = param_map["line_plots"]
        bar_plots = param_map["bar_plots"]
        scatter_plots = param_map["scatter_plots"]

        self._pdf.set_info(player_name, league_df, main_pos)
        self._pdf.set_compare_info(compare_name, league_df, compare_pos)
        self.set_standard_properties(player_name)

        self._pdf.print_comparison_title()
        self.print_player_info()

        self.print_plots(line_plots, bar_plots, scatter_plots)

        return self._pdf.output(dest='S')
