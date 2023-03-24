from abc import ABC, abstractmethod


class Graph(ABC):
    """
    Abstract class representing a Graph and its functionality
    """

    @abstractmethod
    def draw(self, data):
        """
        Method for drawing the graph based on passed data
        """
        pass
