from abc import ABC, abstractmethod


class Graph(ABC):
    """
    Abstract class representing a graph and its functionality
    """

    @abstractmethod
    def draw(self, data) -> any:
        """
        Draws the graph based on passed data

        Parameters:
            data (DataFrame): Dataframe containing relevant data to plot

        Returns:
            any: The image containing the graph
        """
        pass
