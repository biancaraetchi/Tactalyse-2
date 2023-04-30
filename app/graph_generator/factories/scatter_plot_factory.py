from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.scatter_plot import ScattterPlot


class ScatterPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for bar plots"""

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return ScattterPlot()
        else:
            return ScattterPlot()
