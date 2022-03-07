import pandas as pd
import numpy as np
from src.spreadsheet.spreadsheet import Spreadsheet

class OneRSpreadsheet(Spreadsheet):
	def __init__(self, fn):
		self._file_name: str = fn
		self._dataset: pd.DataFrame = None
	
	def is_dataset_set(self):
		""" Checks if dataset attribute is set """
		return True if self._dataset is not None else False

	def get_percentage(self, percent: float) -> int:
		""" Counts the total values and returns the number of items given a percentage """
		total_values = len(self._dataset)
		return int(total_values*percent)
	
	def clean_data(self):
		""" Does a cleansing process in the whole dataframe """
		def whitespaces_cleansing(df: pd.DataFrame):
			""" Removes whitespaces before and after the attribute for every column attributes """
			column_names = list(df)
			for column_name in column_names:
				df[column_name] = df[column_name].astype(str).apply(
					lambda attr: attr.strip()
				)

		print('Dataframe is being cleansed')
		whitespaces_cleansing(self._dataset)

	def randomize_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
		""" Uses dataset to generate a randomized one """
		column_names = list(df)
		numpy_dataset = df.to_numpy()
		np.random.shuffle(numpy_dataset)
		return pd.DataFrame(numpy_dataset, columns=column_names)

	def read(self):
		""" Reads excel file and parses dataframe for retrieving methods """
		self._dataset = pd.read_excel(self._file_name)

		# probably this is redundant
		if self.is_dataset_set() is not True: 
			return 'dataset is not set'
		
		self.clean_data()
		
	def retrieve_test_set(self) -> pd.DataFrame:
		""" Returns the 30% of the dataset randomized """	
		number_of_values = self.get_percentage(0.30)
		test_set = self._dataset[:number_of_values].copy()

		return self.randomize_dataset(test_set) 

	def retrieve_training_set(self) -> pd.DataFrame:
		""" Returns the 70% of the dataset randomized """
		number_of_values = self.get_percentage(0.70)
		training_set = self._dataset[number_of_values:].copy()

		return self.randomize_dataset(training_set)