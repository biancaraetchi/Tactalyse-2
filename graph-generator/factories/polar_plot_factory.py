from factories.abstract_factory import Factory
from graphs.default_graph import DefaultGraph


class PolarPlotFactory(Factory):

    def create_instance(self, obj_type):
        if obj_type != 'Default':
            print("To be implemented.")
        else:
            return DefaultGraph()
