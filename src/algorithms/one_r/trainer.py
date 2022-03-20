import pandas as pd
from src.trainer.trainer import Trainer
from src.spreadsheet.frequency_table import FrequencyTableGenerator


class OneRTrainer(Trainer):

    def __init__(self, target_column: str, frequency_table_generator: FrequencyTableGenerator):
        self._target_column = target_column
        self._frequency_table_generator = frequency_table_generator

        self._model_description = dict()
        self._frequency_tables = list()
        self._rules_to_prove = list()
        self._proven_rules = list()

    def train(self, spreadsheet: pd.DataFrame):
        self._frequency_tables = self._frequency_table_generator.generate(spreadsheet)
        self.__generate_rules()
        self.__calculate_columns_total_error(spreadsheet)
        self.__generate_model_description()

    def __generate_rules(self):
        column_frequency_tables = self._frequency_tables.copy()
        for column_frequency_table in column_frequency_tables:
            column = list(column_frequency_table)[0]
            frequency_table = column_frequency_table[column].items()

            rules = dict()
            last_frequency = 0

            for [column_value, target_column_value], frequency in frequency_table:
                if column_value not in rules:
                    rules[column_value] = target_column_value
                    last_frequency = frequency
                elif frequency > last_frequency:
                    """
                    Just in case that the frequency is greater than the last frequency
                    for the same column value the  **target column value** will be overwritten
                    otherwise the first target column value with the greatest frequency remains
                    as part of the rule. 
                    """
                    rules[column_value] = target_column_value

            column_frequency_table[column] = rules

        self._rules_to_prove = column_frequency_tables

    def __calculate_columns_total_error(self, spreadsheet: pd.DataFrame):
        for column_rules in self._rules_to_prove:
            column_name = list(column_rules)[0]
            rules = column_rules[column_name].copy()

            asserts = 0
            fails = 0

            data_tuples = spreadsheet[[column_name, self._target_column]].itertuples(index=False)
            for [column_value, target_column_value] in data_tuples:
                if rules[column_value] == target_column_value:
                    asserts += 1
                else:
                    fails += 1

            rules["total_error"] = fails / (asserts + fails)
            self._proven_rules.append({column_name: rules})

    def __generate_model_description(self):
        errors = self.__extract_total_error_from_all_columns()
        min_error = min(errors)

        """
        Just for the first match, there could be more rules with the same total_error
        """
        min_error_index = errors.index(min_error)

        self._model_description = self._rules_to_prove[min_error_index]

    def __extract_total_error_from_all_columns(self):
        return [rules["total_error"] for column_rules in self._proven_rules for [_, rules] in column_rules.items()]

    def retrieve_model_description(self):
        return self._model_description
