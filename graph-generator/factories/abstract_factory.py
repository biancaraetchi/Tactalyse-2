from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_instance(self, obj_type):
        pass
