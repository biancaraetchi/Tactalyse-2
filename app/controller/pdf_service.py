from app.pdf_generator.generators.standard_pdf import StandardPDF


def create_pdf(param_map):
    """
    Function that retrieves a generated football analysis report for further use.

    :param league_df: Dataframe containing league data.
    :param player_name: Name of the player to generate a report for.
    :param main_pos: Main position of the player.
    :param radar_chart: Radar chart to be added to the PDF.
    :param line_plot: Line plot to be added to the PDF.
    :return: The PDF generated based on passed parameters and plots, in byte form.
    """
    generator = StandardPDF()
    return generator.generate_pdf(param_map)
