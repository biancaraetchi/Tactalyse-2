from factories.radio_chart_factory import PolarPlotFactory
from graphs.RadioChart import PolarPlot
import matplotlib.pyplot as plt

# Bianca - I'm not sure we need factories for this project...
# generating a whole app for every instance of a plot seems like overkill, if I understand correctly how they work


if __name__ == '__main__':
    """ Temporary main function for testing purposes """

    # plot_factory = PolarPlotFactory()
    # graph = plot_factory.create_instance('Default')
    graph = PolarPlot()
    data = 0

    # Call the draw function and store the result in a variable
    image = graph.draw(data)

    # Display the image using Matplotlib's imshow function
    plt.imshow(image)
    plt.show()


