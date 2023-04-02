from ..graph_generator.factories.radio_chart_factory import RadioChartFactory


def create_polar_plot(player_pos, league_df, columns):
    factory = RadioChartFactory()
    plot_obj = factory.create_instance(player_pos)
    plot = plot_obj.draw(league_df, columns)
    return plot
