from pdf_generator.pdf_generator import generate_basic_pdf


def create_pdf(league_df, player_name, main_pos, plot):
    return generate_basic_pdf(league_df, player_name, main_pos, plot)

