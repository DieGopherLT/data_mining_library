from pprint import pprint

import pandas as pd
from scipy.stats import norm
from functools import reduce

from src.coordinators.trainable_algorithms.tester.interface import Tester


class NaiveBayesTester(Tester):
    def __init__(self, target_column: str):
        self.__target_column = target_column
        self.__model_description = dict()
        self._results = list()
        self.__count_target_values = 0

    def test(self, model_description: dict, test_set: pd.DataFrame):
        self.__model_description = model_description
        probabilities = self.__calculate_probabilities(test_set)
        normalized = self. __normalize_and_predict(probabilities, test_set)
        self.__evaluate(normalized, test_set)

    def retrieve_test_output(self):
        return f'accuracy: {(reduce(lambda x, y: x + y, self._results)/ len(self._results))}'

    def __calculate_probabilities(self, test_set: pd.DataFrame):
        """ Uses a given test_set to calculate and return probabilities """
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

    @staticmethod
    def __get_prediction_target_value_in(prediction, target_values):
        for target_value in target_values:
            if prediction.find(target_value) != -1:
                return target_value

    # this function does both things because doing them separately involves code duplication
    def __normalize_and_predict(self, probabilities: pd.DataFrame, test_set: pd.DataFrame):
        """ Manipulates probabilities and returns a dataframe with calculated normalized values """
        probabilities = probabilities.copy()
        probabilities["normalization"] = None
        probabilities["prediction"] = None

        unique_target_values = test_set[self.__target_column].unique()
        self.__count_target_values = len(unique_target_values)
        rows_to_normalize = int(len(probabilities) / self.__count_target_values)

        for row in range(1, rows_to_normalize + 1):
            instance_group = [f'Pr [ {row} | {column_value} ]' for column_value in unique_target_values]

            grouped_instances = probabilities.loc[instance_group]
            grouped_instances_probabilities = grouped_instances[["probability"]].to_dict()

            for instance_combinations in grouped_instances_probabilities.values():
                probabilities_sum = reduce(lambda x, y: x + y, instance_combinations.values())

                for instance_probability in instance_combinations.items():
                    [index_to_normalize, probability] = instance_probability
                    probabilities.loc[index_to_normalize, "normalization"] = probability / probabilities_sum

            grouped_instances = probabilities.loc[instance_group]
            grouped_instances_normalized = grouped_instances[["normalization"]].to_dict()
            grouped_instances_normalized = grouped_instances_normalized["normalization"]

            prediction = max(grouped_instances_normalized, key=grouped_instances_normalized.get)

            probabilities.loc[instance_group, "prediction"] = self.__get_prediction_target_value_in(prediction, unique_target_values)

        return probabilities

    def __evaluate(self, normalized: pd.DataFrame, test_set: pd.DataFrame):
        normalized_prediction = normalized["prediction"].copy()
        test_set_target_column = test_set[self.__target_column].copy()

        i = 0
        asserts = 0
        for instance in test_set_target_column:
            compared_instance = normalized_prediction[i]
            if instance is compared_instance:
                asserts += 1
            i += self.__count_target_values

        self._results.append(asserts / len(test_set_target_column))
