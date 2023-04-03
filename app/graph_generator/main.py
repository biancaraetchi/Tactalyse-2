import matplotlib.pyplot as plt

from graphs.radio_chart import PolarPlot

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
