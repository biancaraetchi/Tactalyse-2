from ..graph_generator.factories.radio_chart_factory import RadioChartFactory
from ..graph_generator.factories.line_plot_factory import LinePlotFactory


def create_polar_plot(player_pos, league_df, columns):
    factory = RadioChartFactory()
    plot_obj = factory.create_instance(player_pos)
    plot = plot_obj.draw(league_df, columns)
    return plot

def create_line_plot(player_pos, league_df, columns):
    factory = LinePlotFactory()
    plot_obj = factory.create_instance(player_pos)
    plot = plot_obj.draw(league_df, columns)
    return plot
