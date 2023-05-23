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
    # compare_name = "A. Masina"
    # compare_file = "app/pdf_generator/resources/test_data/Player stats I. Sarr.xlsx"
    compare_name = None
    compare_file = None
    start_date = "2016-09-25"
    end_date = "2020-12-23"
    
    radar_map = get_radar_data(league_file, player_name, compare_name)
    line_map = get_line_data(league_file, player_file, player_name, compare_file, compare_name, start_date, end_date) 
    bar_map = get_bar_data(league_file, player_name, compare_name)

    # Pass the maps to get lists containing plots in byte form from the graph_generator module
    radar_chart = create_radar_chart(radar_map)
    line_plots = create_line_plots(line_map)
    bar_plot_set = create_bar_plot_set(bar_map)

    # Get a parameter map with relevant data for generating a PDF from the data module, and pass it to the pdf_generator
    # module along with the graphs
    pdf_map = get_pdf_data(league_file, player_name, compare_name, line_plots, bar_plot_set)
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
