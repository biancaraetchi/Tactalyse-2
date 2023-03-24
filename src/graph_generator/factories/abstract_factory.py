from abc import ABC, abstractmethod
from graph_generator.graphs.abstract_graph import Graph


class Factory(ABC):
    """
    Abstract class representing a factory and its functionality.
    A factory is an object that is able to create a new object based on a passed string parameter, and return it.
    This allows for the instantiation of new objects without knowing the explicit object type.
    """

    @abstractmethod
    def create_instance(self, obj_type):
        """
        Creates a new object instance based on the passed string parameter

        Parameters:
            obj_type (str): The desired object type

        Return:
            object: The object represented by obj_type
        """
        pass
