from abc import ABC, abstractmethod
import pandas as pd


class Tester(ABC):

    @abstractmethod
    def test(self, model_description, test_set: pd.DataFrame):
        pass

    @abstractmethod
    def retrieve_test_output(self):
        pass
