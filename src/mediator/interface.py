from abc import ABC, abstractmethod

from .base_component import MediableComponent


class MachineLearningMediator(ABC):
    
    @abstractmethod
    def notify(self, sender: MediableComponent, event: str):
        pass
    