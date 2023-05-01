from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.bar_plot import *


class BarPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for bar plots"""

    def create_instance(self, param_map):
        graph_type = param_map.get('type')
        params = param_map.get('params')
        if graph_type == 'main_stats':
            return MainStatsBarPlot(params)
        elif graph_type != 'Default':
            print("To be implemented.")
            return BarPlot(params)
        else:
            return BarPlot(params)
