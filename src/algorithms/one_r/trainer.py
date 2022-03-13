import pandas as pd
from src.trainer.trainer import Trainer


class OneRTrainer(Trainer):

    def __init__(self, tc: str):
        self._target_column = tc
        self._model_description = dict()
        self._frequency_tables = list()

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
        rules = dict()
        for frequency_table in self._frequency_tables:
            frequency_table_to_list = list(frequency_table.items())
            sorted_values = sorted(frequency_table_to_list)

            column = sorted_values[0][0]
            children_dict = sorted_values[0][1]

            rules[column] = dict()
            visited = list()

            for tup in children_dict.items():
                column_value = tup[0][0]
                target_value = tup[0][1]
                if column_value not in visited:
                    visited.append(column_value)
                    rules[column][column_value] = target_value

        self._model_description = rules

    def retrieve_model_description(self):
        return self._model_description
