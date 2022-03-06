import pandas as pd

from src.tester.tester import Tester


class ZeroRTester(Tester):
    def test(self, model_description: dict, test_set: pd.Series):

        pass

    def retrieve_test_output(self):
        pass
