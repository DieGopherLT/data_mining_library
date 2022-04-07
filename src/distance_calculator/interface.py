from abc import ABC, abstractmethod


class DistanceCalculator(ABC):
    
    @abstractmethod
    def calculate(self):
        pass

    # @abstractmethod
    # def get_use_case(self):
    #     pass