from app.controller.graph_service import *
from app.controller.data_service import get_bar_data, get_line_data, get_radar_data,get_pdf_data, get_scatter_data
from app.controller.pdf_service import create_pdf
import pandas as pd
import os
import matplotlib

matplotlib.use('TkAgg')


def generate_pdf():
    league_file = "app/pdf_generator/resources/test_data/ENG2.xlsx"
    player_file = "app/pdf_generator/resources/test_data/Player stats T. Cleverley.xlsx"
    player_name = "T. Cleverley"
    compare_name = None
    compare_file = None
    start_date = None
    end_date = None

    radar_map = get_radar_data(league_file, player_name, compare_name)
    line_map = get_line_data(league_file, player_file, player_name, compare_file, compare_name, start_date, end_date)
    bar_map = get_bar_data(league_file, player_name)

    # Pass the maps to get lists containing plots in byte form from the graph_generator module
    radar_chart = create_radar_chart(radar_map)
    line_plots = create_line_plots(line_map)
    bar_plots = create_bar_plots(bar_map, 'v')
    main_stats_bar_plot = create_main_stats_bar_plot(bar_map)

    wtv = {'Interceptions': [1, 2, 4, 2, 6, 3], 'Passes': [3, 4, 2, 7, 4, 2]}
    wtvdf = pd.DataFrame(data=wtv)
    scatter_plot = create_scatter_plot(wtvdf)
    scatter_plots = [scatter_plot, scatter_plot]

    # Get a parameter map with relevant data for generating a PDF from the data module, and pass it to the pdf_generator
    # module along with the graphs
    pdf_map = get_pdf_data(league_file, player_name, compare_name, line_plots, main_stats_bar_plot, scatter_plots)
    pdf_bytes = create_pdf(pdf_map)

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
