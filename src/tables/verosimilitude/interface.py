from abc import ABC, abstractmethod


class VerosimilitudeTable(ABC):

    @abstractmethod
    def retrieve(self):
        pass
