from ..graphs.abstract_models import Graph
import matplotlib.pyplot as plt
import numpy as np
import io


class PolarPlot(Graph):
    """ Class representing a default Graph """
    __position = ''

    def __init__(self, player_pos=None):
        if player_pos:
            self.__position = player_pos
        
    def draw(self, data, column_names):
        print("hiii")
        r = np.arange(0, 2, 0.01)
        theta = 2 * np.pi * r

        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.plot(theta, r)
        ax.set_rmax(2)
        ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
        ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
        ax.grid(True)

        ax.set_title("A template polar plot for position " + self.__position, va='bottom')
        ax.set_ylim([0, 2])
        ax.set_xlim([0, 2*np.pi])

        # Save the plot to a file
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer.getvalue()
