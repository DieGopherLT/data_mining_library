import pandas as pd


class FrequencyTableGenerator:

    def __init__(self, target_column: str):
        self._target_column = target_column

    def generate_with_target_column(self, spreadsheet: pd.DataFrame):
        frequency_tables = list()
        for column in spreadsheet.columns:
            if column == self._target_column:
                continue
            frequency_table = {
                column: spreadsheet[[column, self._target_column]].value_counts().to_dict()
            }
            frequency_tables.append(frequency_table)
        return frequency_tables
