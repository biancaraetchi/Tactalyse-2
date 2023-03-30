from factories.abstract_graph_factory import AbstractGraphFactory
from graphs.models import PolarPlot


class PolarPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for polar plots of each player position """

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return DefaultGraph()
        else:
            return DefaultGraph()
