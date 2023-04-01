from fpdf import FPDF
from pdf_generator import PDF_class


def create_pdf(league_df, player_name, main_pos, plot):
    return PDF_class.generate_pdf(league_df, player_name, main_pos, plot)

