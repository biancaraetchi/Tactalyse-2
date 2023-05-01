from abc import ABC, abstractmethod

from app.pdf_generator.pdf import PDF


class PDFGenerator(ABC):
    def __init__(self):
        self._pdf = PDF()

    def set_standard_properties(self, player_name):
        """
        Function that sets properties like font, color, title and plot size.

        :param player_name:
        """
        self._pdf.alias_nb_pages()
        self._pdf.set_font('Arial', '', 12)
        self._pdf.set_draw_color(250, 51, 10)
        self._pdf.set_fill_color(255, 230, 230)
        self._pdf.set_title(player_name)
        self._pdf.add_page()
        self._pdf.set_plot_properties(145, 100)

    def print_plots(self, line_plots, bar_plots, scatter_plots):
        """
        Function that prints all plots on the report.

        :param line_plots:
        :param bar_plots:
        :param scatter_plots:
        """
        self._pdf.print_chapter('Line Plots', 'These plots showcase player statistics over time.')
        for plot in line_plots:
            self._pdf.print_plot(plot)
        self._pdf.current_y = 70

        self._pdf.print_chapter('Bar Plots',
                                'These plots showcase player statistics compared to those of players in the same position within the league.')
        for plot in bar_plots:
            self._pdf.print_plot(plot)
        self._pdf.current_y = 70
        self._pdf.print_chapter('Scatter Plots',
                                'These plots showcase data in scatter plots.')
        for plot in scatter_plots:
            self._pdf.print_plot(plot)
        self._pdf.current_y = 70

    @abstractmethod
    def print_player_info(self):
        """
        Function that prints standard player info on (an) introductory page(s).
        """
        pass

    @abstractmethod
    def generate_pdf(self, param_map):
        """
        Function that takes a parameter map with data to show on the report, and returns a completed PDF.

        :param param_map: Map containing parameter names as keys, and their values as values.
        :return: A completed PDF report in byte form.
        """
        pass

    @property
    def pdf(self):
        """
        Getter for the PDFGenerator object's pdf field variable, an object representing the PDF.

        :return: A PDF object representing the report.
        """
        return self._pdf
