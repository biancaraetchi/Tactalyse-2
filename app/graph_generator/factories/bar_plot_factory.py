from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.bar_plot import BarPlot
from ..graphs.clustered_bar_plot import ClusteredBarPlot
from ..graphs.leaderboard_bar_plot import LeaderboardBarPlot

class BarPlotFactory(AbstractGraphFactory):
    """ Class representing a factory for bar plots"""

    def create_instance(self, param_map):
        graph_type = param_map.get('type')
        params = param_map.get('params')
        if graph_type == 'clustered':
            return ClusteredBarPlot(params)
        elif graph_type == 'leaderboard':
            return LeaderboardBarPlot(params)
        elif graph_type != 'Default':
            print("To be implemented.")
            return BarPlot(params)
        else:
            return BarPlot(params)
