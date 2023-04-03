from ..data.preprocessing import radio_chart_data
from ..data.preprocessing import line_plot_data


def get_radio_chart_data(league_file, player_name):
    return radio_chart_data(league_file, player_name)

def get_line_plot_data(league_file, player_name):
    return line_plot_data(league_file, player_name)
