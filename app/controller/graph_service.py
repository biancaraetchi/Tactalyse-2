from ..graph_generator.factories.bar_plot_factory import BarPlotFactory
from ..graph_generator.factories.line_plot_factory import LinePlotFactory
from ..graph_generator.factories.radar_chart_factory import RadarChartFactory
from ..graph_generator.factories.scatter_plot_factory import ScatterPlotFactory


def create_radar_chart(radar_map):
    """
    Function that retrieves a drawn radio chart for further use.

    :param radar_map:
    :return: The radio chart drawn based on passed parameters, in byte form.
    """
    factory = RadarChartFactory()
    param_map = {'type': 'Default', 'params': radar_map}
    plot_obj = factory.create_instance(param_map)
    plot = plot_obj.draw(radar_map)
    return plot


def create_line_plots(line_map):
    """
    Function that retrieves a drawn line plot for further use.

    :param line_map:
    :return: The line plot drawn based on passed parameters, in byte form.
    """
    factory = LinePlotFactory()
    param_map = {'type': 'Default', 'params': line_map}
    plot_obj = factory.create_instance(param_map)
    plots = plot_obj.draw_all(line_map)
    return plots


def create_bar_plots(bar_map, orientation):
    """
    Function that retrieves a drawn bar plot for further use.

    :param bar_map:
    :return: The bar plot drawn based on passed parameters, in byte form.
    """
    factory = BarPlotFactory()
    param_map = {'type': 'Default', 'params': bar_map}
    bar_map.update({"orientation": orientation})
    plot_obj = factory.create_instance(param_map)
    plots = plot_obj.draw_all(bar_map)
    return plots

def create_main_stats_bar_plot(bar_map):
    factory = BarPlotFactory()
    param_map = {'type': 'main_stats', 'params': bar_map}
    plot_obj = factory.create_instance(param_map)
    return plot_obj.draw(bar_map)

def create_scatter_plots(scatter_map):
    """
    Function that retrieves a drawn scatter plot for further use.

    :param scatter_map:
    :return: The scatter plot drawn based on passed parameters, in byte form.
    """
    factory = ScatterPlotFactory()
    plot_obj = factory.create_instance("Default")
    plot = plot_obj.draw_all(scatter_map)

    return plot
