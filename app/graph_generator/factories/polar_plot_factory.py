from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.PolarPlot import PolarPlot


class PolarPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for polar plots of each player position """

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return PolarPlot(graph_type)
        else:
            return PolarPlot()
