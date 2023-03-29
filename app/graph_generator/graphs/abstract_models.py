from abc import ABC, abstractmethod


class Graph(ABC):
    """
    Abstract class representing a graph and its functionality
    """
    @abstractmethod
    def __init__(self):
        """
        Constructor for graphs
        """
        pass

    @abstractmethod
    def draw(self, data, column_names) -> any:
        """
        Draws the graph based on passed data

        Parameters:
            data (DataFrame): Dataframe containing relevant data to plot
            column_names: array of co

        Returns:
            any: The image containing the graph
        """
        pass
