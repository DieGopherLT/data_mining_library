import pandas as pd
from src.trainer.trainer import Trainer


class OneRTrainer(Trainer):

    def __init__(self, tc: str):
        self._target_column = tc
        self._model_description = dict()
        self._frequency_tables = list()
        self._rules_to_prove = list()

    def train(self, spreadsheet: pd.DataFrame):
        self._frequency_tables = self.__generate_frequency_tables(spreadsheet)
        self.__generate_rules()

    def __generate_frequency_tables(self, ss: pd.DataFrame) -> list:
        frequency_tables = list()
        for col in ss.columns:
            if col == self._target_column:
                continue
            frequency_table = {
                col: ss[[col, self._target_column]].value_counts().to_dict()
            }
            frequency_tables.append(frequency_table)
        return frequency_tables

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

    def retrieve_model_description(self):
        return self._model_description
