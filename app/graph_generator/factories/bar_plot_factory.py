from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.bar_plot import BarPlot


class BarPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for bar plots"""

    def create_instance(self, player_name, graph_type, orientation):
        if graph_type != 'Default':
            print("To be implemented.")
            return BarPlot(player_name, graph_type, orientation)
        else:
            return BarPlot()
