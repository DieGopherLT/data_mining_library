import pandas as pd
from scipy.stats import norm
from functools import reduce

from src.coordinators.trainable_algorithms.tester.interface import Tester


class NaiveBayesTester(Tester):
    def __init__(self, target_column: str):
        self.__target_column = target_column
        self.__model_description = {}
        self._result = pd.DataFrame

    def test(self, model_description: dict, test_set: pd.DataFrame):
        self.__model_description = model_description
        self.__calculate_probability(test_set)

    def retrieve_test_output(self):
        pass

    def __calculate_probability(self, test_set: pd.DataFrame):
        columns = list(test_set.columns)
        enum_column = list(enumerate(test_set.columns))
        enum_column = {column: index for [index, column] in enum_column}

        output_df = pd.DataFrame(columns=columns)

        instances = test_set.itertuples(index=False)

        target_column = self.__target_column
        target_column_values = test_set[target_column].unique()

        i = 0  # Number of instance
        for instance in instances:
            i += 1
            for target_column_value in target_column_values:
                factors = {}

                for column in columns:
                    attr = enum_column[column]

                    column_keys = self.__model_description[column].keys()

                    if column == target_column:
                        factors[column] = self.__model_description[column][target_column_value]

                    elif ("avg" or "std") in column_keys:
                        mean = self.__model_description[column]["avg"][target_column_value]
                        std = self.__model_description[column]["std"][target_column_value]
                        pdf = norm.pdf(getattr(instance, f'_{attr}'), mean, std)
                        factors[column] = pdf

                    else:
                        factors[column] = self.__model_description[column][target_column_value][getattr(instance, f'_{attr}')]

                probability = reduce(lambda x, y: x*y, factors.values())

                factors["probability"] = probability

                row = pd.DataFrame(
                    factors
                , index=[f'Pr [ { i } | {target_column_value} ]'])

                output_df = pd.concat([output_df, row])
