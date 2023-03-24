from abc import ABC, abstractmethod


class Graph(ABC):
    """
    Abstract class representing a graph and its functionality
    """

    @abstractmethod
    def draw(self, data) -> bytes:
        """
        Draws the graph based on passed data

        Parameters:
            data (DataFrame): Dataframe containing relevant data to plot

        Returns:
            bytes: The image containing the graph in bytes
        """
        pass
