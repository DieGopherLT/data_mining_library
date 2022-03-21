import pandas as pd
from collections import Counter
from src.coordinators.trainable_algorithms.trainer.interface import Trainer


class ZeroRTrainer(Trainer):

    def __init__(self):
        self._model_description = ""

    def train(self, spreadsheet: pd.Series) -> None:
        target_class_values = spreadsheet.tolist()
        values_counter = dict(Counter(target_class_values))
        self._model_description = max(values_counter, key=values_counter.get)

    def retrieve_model_description(self) -> str:
        return self._model_description
