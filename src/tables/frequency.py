from abc import ABC, abstractmethod
import pandas as pd


class FrequencyTableGenerator(ABC):

    @abstractmethod
    def generate(self, spreadsheet: pd.DataFrame):
        pass


class FrequencyTableWithoutZeros(FrequencyTableGenerator):

    def __init__(self, target_column: str):
        self._target_column = target_column

    def generate(self, spreadsheet: pd.DataFrame):
        frequency_tables = list()
        for column in spreadsheet.columns:
            if column == self._target_column:
                continue
            frequency_table = {
                column: spreadsheet[[column, self._target_column]].value_counts().to_dict()
            }
            frequency_tables.append(frequency_table)
        return frequency_tables


class FrequencyTableWithZeros(FrequencyTableGenerator):

    def __init__(self, target_column: str):
        self._target_column = target_column

    def generate(self, spreadsheet: pd.DataFrame):
        frequency_tables = list()
        for column in spreadsheet.columns:
            if column == self._target_column:
                continue
            frequency_table = {
                column: pd.crosstab(spreadsheet[column], spreadsheet[self._target_column]).to_dict()
            }
            frequency_tables.append(frequency_table)
        return frequency_tables
