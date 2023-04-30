from app.controller.graph_service import *
from app.controller.data_service import get_bar_data, get_line_data, get_radar_data
from app.controller.pdf_service import create_pdf
from app.data.preprocessor import Preprocessor
from placeholder_graphs import generate_placeholders
import os
import matplotlib

matplotlib.use('TkAgg')


def generate_pdf():
    league_file = "app/pdf_generator/resources/test_data/ENG2.xlsx"
    player_file = "app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx"
    player_name = "T. Cleverley"
    processor = Preprocessor()

    league_df = get_bar_data(league_file)
    player_row, columns_radio_chart, main_pos_long, main_pos = get_radar_data(processor, league_file, player_name)
    player_data, columns_line_plot = get_line_data(player_file, main_pos)

    radar_chart = create_radar_chart(main_pos_long, player_row, columns_radio_chart)
    line_plot = create_line_plot(None, player_data, columns_line_plot)
    bar_plot = create_bar_plot(player_name, main_pos, league_df, player_row, "Goals", 'v')

    params = {"league_df": league_df, "player_name": player_name, "main_pos": main_pos_long, "line_plots": [line_plot,
                                                                                                            line_plot],
              "bar_plots": [bar_plot, bar_plot, bar_plot]}
    pdf_bytes = create_pdf(params)

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
