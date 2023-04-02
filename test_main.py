from app.controller.graph_service import create_polar_plot
from app.controller.data_service import read_files_standard, get_column_names, get_main_position, get_player_row
from app.controller.pdf_service import create_pdf
import os
import matplotlib
matplotlib.use('TkAgg')


def generate_pdf():

    league_file = "app/pdf_generator/resources/test_data/ENG2.xlsx"
    player_file = "app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx"
    player_name = "T. Cleverley"

    league_df, player_df = read_files_standard(league_file, player_file)
    player_row = get_player_row(league_df, player_name)
    main_pos = get_main_position(player_row)
    print(main_pos)
    columns = get_column_names(main_pos)
    print(columns)

    plot = create_polar_plot(main_pos, player_row, columns)

    pdf_bytes = create_pdf(league_df, player_name, main_pos, plot)

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
