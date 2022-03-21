import pandas as pd
from abc import ABC, abstractmethod


class Trainer(ABC):

    @abstractmethod
    def train(self, training_set: pd.DataFrame):
        pass

    @abstractmethod
    def retrieve_model_description(self):
        pass
