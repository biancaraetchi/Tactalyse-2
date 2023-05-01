from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.scatter_plot import ScatterPlot


class ScatterPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for scatter plots"""

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return ScatterPlot()
        else:
            return ScatterPlot()
