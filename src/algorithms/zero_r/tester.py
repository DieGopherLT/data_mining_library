import pandas as pd

from src.coordinators.trainable_algorithms.tester.interface import Tester


class ZeroRTester(Tester):
    def __init__(self):
        self._model_description = ""
        self._result = {}

    def test(self, model_description: str, test_set: pd.Series):
        self._model_description = model_description
        asserts = test_set.apply(self.asserts_fun)
        self._result = asserts.value_counts().to_dict()

    def retrieve_test_output(self):
        return self._result

    def asserts_fun(self, x):
        return "Succeed" if x == self._model_description else "FAIL"
