from factories.polar_plot_factory import PolarPlotFactory


if __name__ == '__main__':
    """ Temporary main function for testing purposes """

    plot_factory = PolarPlotFactory()
    dg = plot_factory.create_instance('Default')
    data = 0
    dg.draw(data)
