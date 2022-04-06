from abc import ABC, abstractmethod


class DistanceCalculator(ABC):
    
    @abstractmethod
    def calculate(self):
        pass
    