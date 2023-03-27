from abc import ABC, abstractmethod
from graph_generator.graphs.abstract_graph import Graph


class AbstractGraphFactory(ABC):
    """
    Abstract class representing a graph factory and its functionality.
    A graph factory is an object that is able to create a new graph based on a passed string parameter, and return it.
    This allows for the instantiation of new graphs without knowing the explicit graph type.
    """

    @abstractmethod
    def create_instance(self, graph_type) -> Graph:
        """
        Creates a new graph instance based on the passed string parameter

        Parameters:
            graph_type (str): The desired graph type

        Return:
            Graph: The graph object represented by graph_type
        """
        pass
