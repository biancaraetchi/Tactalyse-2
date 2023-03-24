from graph_generator.factories.abstract_factory import Factory
from graph_generator.graphs.default_graph import DefaultGraph


class LinePlotFactory(Factory):
    """ Class representing a factory for line plots of each player position """

    def create_instance(self, obj_type):
        if obj_type != 'Default':
            print("To be implemented.")
        else:
            return DefaultGraph()
