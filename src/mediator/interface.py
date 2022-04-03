from abc import ABC, abstractmethod


class MachineLearningMediator:
    
    @abstractmethod
    def notify(self, event: str):
        pass
    