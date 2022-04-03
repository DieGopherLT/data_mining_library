from abc import ABC, abstractmethod


class DistanceCalculator(ABC):
    
    @abstractmethod
    def caclulate(self):
        pass
    