import pandas as pd
import numpy as np

from src.spreadsheet.spreadsheet import Spreadsheet
from src.spreadsheet.reader import SpreadsheetReader
from src.spreadsheet.cleaner import SpreadsheetCleaner

from src.spreadsheet.exception import SpreadsheetNotSetError, TargetColumnNotFoundError, TargetColumnError

class ZeroRSpreadsheet(Spreadsheet):
	def __init__(self, file: str, reader: SpreadsheetReader, cleaner: SpreadsheetCleaner):
		self.__reader: SpreadsheetReader = reader
		self.__cleaner: SpreadsheetCleaner = cleaner

		self._file_name: str = file
		self._target_column: str = None

		self._dataset: pd.DataFrame = None
		self._parsed_dataset: pd.Series = None
		self._randomized_parsed_dataset: pd.Series = None

	def is_dataset_set(self) -> bool:
		""" Checks if dataset attribute is set """
		return True if self._dataset is not None else False

	def is_target_set(self) -> bool:
		""" Checks if target_column attribute is set """
		return True if self.target_column is not None else False
	
	def is_target_column_ok(self) -> bool:
		""" Checks if target_column is a valid column of the dataset """
		column_names = list(self._dataset)	
		return True if self.target_column in column_names else False

	def set_target_column(self, tc):
		""" Sets the column that would be the target to analyzed by the algorithm """
		self.target_column = tc

	def get_percentage(self, percent) -> int:
		""" Counts the total values and returns the number of items given a percentage """
		total_values = len(self._parsed_dataset)
		return int(total_values*percent)

	def parse_data(self):
		""" Parses target column ready to be passed to Trainer class """ 
		self._parsed_dataset = self._dataset[self.target_column].squeeze()	
	
	def clean_data(self):
		""" Does a cleansing process for target column """

		print(f'Target column: < {self.target_column} > is being cleansed...')
		self._dataset = self.__cleaner.clean(self._dataset)

	def randomize_dataset(self):
		""" Uses dataset to create a randomized one """
		numpy_dataset_series = self._parsed_dataset.to_numpy()
		np.random.shuffle(numpy_dataset_series)
		self._randomized_parsed_dataset = pd.Series(numpy_dataset_series)

	def read(self):
		""" Reads excel file and parses dataframe for retrieving methods """

		self._dataset = self.__reader.read_file(self._file_name)

		if self.is_dataset_set() is not True:
			SpreadsheetNotSetError()
		if self.is_target_set() is not True:
			TargetColumnError()
		if self.is_target_column_ok() is not True:
			TargetColumnNotFoundError()

		self.clean_data()
		self.parse_data()

	def retrieve_test_set(self) -> pd.Series:
		""" Returns the 30% of the randomized parsed dataset """
		self.randomize_dataset()
		number_of_values = self.get_percentage(0.30)

		test_set = self._randomized_parsed_dataset[:number_of_values]
		return test_set
			
	def retrieve_training_set(self) -> pd.Series:
		""" Returns the 70% of the randomized parsed dataset """
		self.randomize_dataset()
		number_of_values = self.get_percentage(0.70)	

		training_set = self._randomized_parsed_dataset[:number_of_values]

		return training_set