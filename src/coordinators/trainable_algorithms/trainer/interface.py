from abc import ABC, abstractmethod


class Trainer(ABC):

    @abstractmethod
    def train(self, training_set):
        pass

    @abstractmethod
    def retrieve_model_description(self):
        pass
