from graph_generator.factories.abstract_graph_factory import AbstractGraphFactory
from graph_generator.graphs.default_graph import DefaultGraph


class LinePlotFactory(AbstractGraphFactory):
    """ Class representing a factory for line plots of each player position """

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return DefaultGraph()
        else:
            return DefaultGraph()
