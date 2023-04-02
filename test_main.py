from app.controller.graph_service import create_radio_chart
from app.controller.data_service import get_radio_chart_data
from app.controller.pdf_service import create_pdf
import os
import matplotlib
matplotlib.use('TkAgg')


def generate_pdf():

    league_file = "app/pdf_generator/resources/test_data/ENG2.xlsx"
    player_file = "app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx"
    player_name = "T. Cleverley"

    player_row, columns, main_pos = get_radio_chart_data(league_file, player_name)

    plot = create_radio_chart(None, player_row, columns)

    pdf_bytes = create_pdf(player_row, player_name, main_pos, plot)

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
