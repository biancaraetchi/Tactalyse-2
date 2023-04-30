from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.line_plot import LinePlot


class LinePlotFactory(AbstractGraphFactory):
    """ Class representing a factory for line plots of each player position """

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return LinePlot(graph_type)
        else:
            return LinePlot()
