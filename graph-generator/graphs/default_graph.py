from graphs.abstract_graph import Graph
import matplotlib.pyplot as plt
import numpy as np


class DefaultGraph(Graph):
    """ Class representing a default Graph """

    def draw(self, data):
        print("hiii")
        r = np.arange(0, 2, 0.01)
        theta = 2 * np.pi * r

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.plot(theta, r)
        ax.set_rmax(2)
        ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
        ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
        ax.grid(True)

        ax.set_title("A line plot on a polar axis", va='bottom')
        plt.show()
