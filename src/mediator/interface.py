from abc import ABC, abstractmethod


class MachineLearningMediator(ABC):
    
    @abstractmethod
    def notify(self, sender: object, event: str):
        pass
