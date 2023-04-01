from fpdf import FPDF
import pandas as pd
import os
from . import PDF_class

class pdf_gen_class:
    def generate_pdf(league_df, player_name, main_pos, plot):
        pdf = PDF_class.PDF()

        pdf.player_name = player_name
        pdf.player_position = main_pos
        pdf.player_height = league_df.loc[player_name, 'Height']
        pdf.player_DOB = "13/03/1997"   
        pdf.player_agent = "temp2"
        pdf.player_age = league_df.loc[player_name, 'Age']
        pdf.player_country = league_df.loc[player_name, 'Birth country']
        pdf.player_club = league_df.loc[player_name, 'Team']
        pdf.player_league = "temp7"
        pdf.player_weight = league_df.loc[player_name, 'Weight']
        pdf.player_foot = league_df.loc[player_name, 'Foot']
        pdf.player_on_loan = league_df.loc[player_name, 'On loan']
        pdf.player_contract_date = league_df.loc[player_name, 'Contract expires']
        pdf.player_num_matches = league_df.loc[player_name, 'Matches played']

        pdf.graph1 = plot

        pdf.alias_nb_pages()
        pdf.set_font('Arial', '', 12)
        pdf.set_draw_color(250, 51, 10)
        pdf.set_fill_color(255, 230, 230)
        pdf.set_title(pdf.player_name)
        pdf.add_page()
        pdf.print_title()
        pdf.print_player_basic_info()
        pdf.print_chapter('Stats Progression', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
        return pdf.output(pdf.title + '.pdf', 'S')
    
