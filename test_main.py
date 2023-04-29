from app.controller.graph_service import *
from app.controller.data_service import get_league_data, get_player_data, get_all_league_data
from app.controller.pdf_service import create_pdf
from placeholder_graphs import generate_placeholders
import os
import matplotlib
matplotlib.use('TkAgg')


def generate_pdf():

    league_file = "app/pdf_generator/resources/test_data/ENG2.xlsx"
    player_file = "app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx"
    player_name = "T. Cleverley"

    league_df = get_all_league_data(league_file)
    player_row, columns_radio_chart, main_pos_long, main_pos = get_league_data(league_file, player_name)
    player_data, columns_line_plot = get_player_data(player_file, main_pos)

    radar_chart = create_radio_chart(main_pos_long, player_row, columns_radio_chart)
    line_plot = create_line_plot(None, player_data, columns_line_plot)
    bar_plot = create_bar_plot(player_name, main_pos_long, league_df, player_row, "Goals", 'v')

    pdf_bytes = create_pdf(player_row, player_name, main_pos_long, radar_chart, line_plot, bar_plot)

    # Save the PDF to a file
    with open("test.pdf", "wb") as f:
        f.write(pdf_bytes)

    # Open the PDF file using the default PDF viewer
    if os.name == 'nt':  # For Windows
        os.startfile("test.pdf")
    else:  # For macOS and Linux
        os.system("open test.pdf")


if __name__ == "__main__":
    generate_pdf()
