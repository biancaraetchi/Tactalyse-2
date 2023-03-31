from controller.graph_service import create_polar_plot
from controller.data_service import read_files_standard, get_column_names, get_main_position
import matplotlib.pyplot as plt


def generate_pdf():
    league_file = "../ENG2.xlsx"
    player_file = "../T._Cleverley.xlsx"
    player_name = "T. Cleverley"

    league_df, player_df = read_files_standard(league_file, player_file)
    columns = get_column_names(player_df)
    main_pos = get_main_position(league_df, player_name)

    plot = create_polar_plot(main_pos, player_df, columns)

    # Display the image using Matplotlib's imshow function
    plt.imshow(plot)
    plt.show()


generate_pdf()
