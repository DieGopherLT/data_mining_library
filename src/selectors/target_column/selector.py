import pandas as pd
from ..exception import OutOfRange

from ...spreadsheet.reader import SpreadsheetReader
from ...spreadsheet.cleaner import SpreadsheetCleaner


class TargetColumnSelector:
    
	def __init__(self, reader: SpreadsheetReader, cleaner: SpreadsheetCleaner):
		self._reader = reader
		self._cleaner = cleaner

	def print_column_selector(self, column_names: list):
		for i in range(len(column_names)):
			print(f'[{i+1}] {column_names[i]}')

	def print_dataset_preview(self, dataset: pd.DataFrame, rows: int):
		print(dataset[:rows])	

	def select_target_column_in(self, file_name: str, rows: int) -> str:
		dataset = self._reader.read_file(file_name)
		dataset = self._cleaner.clean_column_names_whitespaces(dataset)

		column_names = dataset.columns

		ok = False 
		while(ok == False):
			print('Dataset preview:\n')
			self.print_dataset_preview(dataset, rows)

			print('\nColumns:\n')
			self.print_column_selector(column_names)

			target_column_index = int(input('\nSelect target column: '))

			try:
				OutOfRange(target_column_index, len(column_names))
			except IndexError:
				print(f'{target_column_index} is not a proper index of the columns.')
				continue
			ok = True

		target_column = column_names[target_column_index-1]
		return target_column
