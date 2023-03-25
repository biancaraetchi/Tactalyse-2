from graph_generator.factories.polar_plot_factory import PolarPlotFactory
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io


if __name__ == '__main__':
    """ Temporary main function for testing purposes """

    plot_factory = PolarPlotFactory()
    graph = plot_factory.create_instance('Default')
    data = 0

    # Call the draw function and store the result in a variable
    image = graph.draw(data)

    # Display the image using Matplotlib's imshow function
    plt.imshow(image)
    plt.show()


