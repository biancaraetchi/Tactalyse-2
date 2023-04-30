from ..graph_generator.factories.line_plot_factory import LinePlotFactory
from ..graph_generator.factories.radar_chart_factory import RadarChartFactory
from ..graph_generator.factories.bar_plot_factory import BarPlotFactory


def create_radio_chart(main_pos, player_row, columns):
    """
    Function that retrieves a drawn radio chart for further use.

    :param main_pos: Main position of the player whose stats to graph.
    :param player_row: Dataframe containing league data of the player whose stats to graph.
    :param columns: List of columns to use from the league dataframe.
    :return: The radio chart drawn based on passed parameters, in byte form.
    """
    factory = RadarChartFactory()
    plot_obj = factory.create_instance(main_pos)
    plot = plot_obj.draw(player_row, columns)
    return plot


def create_line_plot(main_pos, player_df, columns):
    """
    Function that retrieves a drawn line plot for further use.

    :param main_pos: Main position of the player whose stats to graph.
    :param player_df: Dataframe containing match data of the player whose stats to graph.
    :param columns: List of columns to use from the player dataframe.
    :return: The line plot drawn based on passed parameters, in byte form.
    """
    factory = LinePlotFactory()
    plot_obj = factory.create_instance(main_pos)
    plot = plot_obj.draw(player_df, columns)
    return plot

def create_bar_plot(player_name, main_pos, league_df, player_league_row_df, columns, orientation):
    """
    Function that retrieves a drawn bar plot for further use.

    :param main_pos: Main position of the player whose stats to graph.
    :param pl_league_df: Dataframe containing data of the league the player plays in.

    :param columns: List of columns to use from the league dataframe.
    :return: The bar plot drawn based on passed parameters, in byte form.
    """
    factory = BarPlotFactory()
    plot_obj = factory.create_instance(player_name, main_pos, 'PlayerVsAvg', orientation)
    plot = plot_obj.draw(league_df, columns)
    
    return plot
