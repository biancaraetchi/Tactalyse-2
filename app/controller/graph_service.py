from graph_generator.factories.polar_plot_factory import PolarPlotFactory
import matplotlib.pyplot as plt


def create_polar_plot(player_pos, player_df, columns):
    factory = PolarPlotFactory()
    plot = factory.create_instance(player_pos)
    png = plot.draw(player_df, columns)
    return png
