from ..factories.abstract_graph_factory import AbstractGraphFactory
from ..graphs.radio_chart import RadioChart


class RadioChartFactory(AbstractGraphFactory):
    """ Class representing a factory for polar plots of each player position """

    def create_instance(self, graph_type):
        if graph_type != 'Default':
            print("To be implemented.")
            return RadioChart(graph_type)
        else:
            return RadioChart()
