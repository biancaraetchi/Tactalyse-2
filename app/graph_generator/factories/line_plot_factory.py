from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.line_plot import LinePlot


class LinePlotFactory(AbstractGraphFactory):
    """ Class representing a factory for line plots of each player position """

    def create_instance(self, param_map):
        """
        Function that creates an instance of a line plot depending on the passed parameter map's 'type' key's value.
        """
        graph_type = param_map.get('type')
        params = param_map.get('params')
        if graph_type != 'Default':
            print("To be implemented.")
            return LinePlot(params)
        else:
            return LinePlot(params)
