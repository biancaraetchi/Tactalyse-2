from ..pdf_generator.pdf_generator import generate_basic_pdf


def create_pdf(league_df, player_name, main_pos, plots):
    """
    Function that retrieves a generated football analysis report for further use.

    :param league_df: Dataframe containing league data.
    :param player_name: Name of the player to generate a report for.
    :param main_pos: Main position of the player.
    :param plots: Plots to be added to the PDF.
    :return: The PDF generated based on passed parameters and plots, in byte form.
    """
    return generate_basic_pdf(league_df, player_name, main_pos, plots)
