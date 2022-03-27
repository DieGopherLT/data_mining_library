from pprint import pprint

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
        probabilities = self.__calculate_probabilities(test_set)
        # print(probabilities)
        self.__normalize(probabilities, test_set)

    def retrieve_test_output(self):
        pass

    def __calculate_probabilities(self, test_set: pd.DataFrame):
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
                        factors[column] = self.__model_description[column][target_column_value][
                            getattr(instance, f'_{attr}')]

                probability = reduce(lambda x, y: x * y, factors.values())

                factors["probability"] = probability

                row = pd.DataFrame(
                    factors
                    , index=[f'Pr [ {i} | {target_column_value} ]'])

                output_df = pd.concat([output_df, row])

        return output_df

    def __normalize(self, probabilities: pd.DataFrame, test_set: pd.DataFrame):
        target_column_values = test_set[self.__target_column].unique()
        target_column_values_count = len(target_column_values)
        rows_to_normalize = int(len(probabilities) / target_column_values_count)

        instance_group = list() # Is just here for the demo
        for row in range(1, rows_to_normalize + 1):
            instance_group = [f'Pr [ {row} | {column_value} ]' for column_value in target_column_values]

        # This is also here just for testing, should be idented one more level inside for line 80
        grouped_instances = probabilities.loc[instance_group]
        grouped_instances_dict = grouped_instances[["probability"]].to_dict()

        for instance_probability in grouped_instances_dict.values():
            normalized = dict()
            for ins_pr in instance_probability.items():
                [pr_value_given, probability] = ins_pr
                # print(pr_value_given, probability)
                other_probabilities = dict(filter(lambda e: e != ins_pr, instance_probability.items()))
                pprint(other_probabilities)
                values_sum = reduce(lambda x, y: x + y, other_probabilities.values())
                print(values_sum)
                normalized[pr_value_given] = probability / values_sum

            pprint(normalized)


