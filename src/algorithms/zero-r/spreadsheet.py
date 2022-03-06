import pandas as pd
import numpy as np
from src.spreadsheet.spreadsheet import Spreadsheet

class ZeroRSpreadsheet(Spreadsheet):
	def __init__(self, fn):
		self._file_name: str = fn 
		self._dataset: pd.DataFrame = None
		self._parsed_dataset: pd.Series = None
		self.target_column: str = None
		self._randomized_parsed_dataset: pd.Series = None

	def is_dataset_set(self):
		""" Checks if dataset attribute is set """
		return True if self._dataset is not None else False

	def is_target_set(self):
		""" Checks if target_column attribute is set """
		return True if self.target_column is not None else False
	
	def is_target_column_ok(self):
		""" Checks if target_column is a valid column of the dataset """
		column_names = list(self._dataset)	
		return True if self.target_column in column_names else False

	def set_target_column(self, tc):
		""" Sets the column that would be the target to analyzed by the algorithm """
		self.target_column = tc

	def get_percentage(self, percent):
		total_values = len(self._parsed_dataset)
		return int(total_values*percent)

	def parse_data(self) -> pd.Series:
		""" Parses target column ready to be passed to Trainer class """ 
		self._parsed_dataset = self._dataset[self.target_column].squeeze()	
	
	def randomize_dataset(self) -> pd.Series:
		""" Uses dataset to create a randomized one """
		numpy_dataset_series = self._parsed_dataset.to_numpy()
		np.random.shuffle(numpy_dataset_series)
		self._randomized_parsed_dataset = pd.Series(numpy_dataset_series)

	def read(self):
		""" Reads excel file and parses dataframe for retrieving methods """
		self._dataset = pd.read_excel(self._file_name)

		if self.is_dataset_set() is not True:
			return 'dataset is not set'
		if self.is_target_set() is not True:
			return 'target column is not set'
		if self.is_target_column_ok() is not True:
			return 'target column not found in the column names of the dataset'

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