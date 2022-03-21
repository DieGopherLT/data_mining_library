import pandas as pd

from ...spreadsheet.reader import SpreadsheetReader


class TargetColumnSelector:
    
	def __init__(self, reader: SpreadsheetReader):
		self._reader = reader

	def clean_column_names(self, columns: list): # TODO: This could be on Spreadsheet-Cleaner
		cleaned_columns = list()
		for column in columns:
			cleaned_columns.append(column.strip())
		return cleaned_columns

	def print_column_selector(self, column_names: list):
		for i in range(len(column_names)):
			print(f'[{i+1}] {column_names[i]}')

	def print_dataset_preview(self, dataset: pd.DataFrame, rows: int):
		print(dataset[:rows])	

	def select_target_column_in(self, file_name: str, rows: int) -> str:
		dataset = self._reader.read_file(file_name)
		column_names = self.clean_column_names(list(dataset))

		print('Dataset preview:\n')
		self.print_dataset_preview(dataset, rows)

		print('\nColumns:\n')
		self.print_column_selector(column_names)

		target_column_index = int(input('\nSelect target column: '))
		target_column = column_names[target_column_index-1]

		return target_column
