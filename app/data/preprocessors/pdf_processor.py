from app.data.excel_reader import ExcelReader
from .preprocessor import Preprocessor


class PDFProcessor(Preprocessor):
    def params_to_map(self, league_file, player_name, league_name, compare_name, line_plots, bar_plots,
                      player_image=None, player_cmp_image=None):
        """
        Function that extracts all required data from the passed league data Excel file, along with passed parameters
        required for PDF generation.

        :param league_file:
        :param player_name:
        :param league_name:
        :param compare_name:
        :param line_plots:
        :param bar_plots:
        :param player_image:
        :param player_cmp_image:
        :return: Map containing data required for generating a bar plot.
        """
        reader = ExcelReader()
        league_df = reader.league_data(league_file, player_name, compare_name)
        pdf_map = {'league_data': league_df}

        pdf_map.update({'player_name': player_name})
        player_row = self.extract_player(league_df, player_name)
        main_pos = self.main_position(player_row)
        main_pos = self.position_dictionary().get(main_pos)
        pdf_map.update({'main_pos': main_pos})
        pdf_map.update({'league': league_name})

        if compare_name:
            pdf_map.update({'compare_name': compare_name})
            compare_row = self.extract_player(league_df, compare_name)
            compare_pos = self.main_position(compare_row)
            compare_pos = self.position_dictionary().get(compare_pos)
            pdf_map.update({'compare_pos': compare_pos})
        else:
            pdf_map.update({'compare_name': None})
            pdf_map.update({'compare_pos': None})

        pdf_map.update({'line_plots': line_plots})
        pdf_map.update({'bar_plots': bar_plots})

        pdf_map.update({'player_image': player_image})
        pdf_map.update({'player_cmp_image': player_cmp_image})

        return pdf_map
