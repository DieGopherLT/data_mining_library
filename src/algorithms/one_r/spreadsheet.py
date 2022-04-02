import pandas as pd
import numpy as np

from src.spreadsheet.spreadsheet import Spreadsheet
from src.spreadsheet.reader import SpreadsheetReader
from src.spreadsheet.cleaner import SpreadsheetCleaner

from src.spreadsheet.exception import SpreadsheetNotSetError

class OneRSpreadsheet(Spreadsheet):
	def __init__(self, file:str, reader: SpreadsheetReader, cleaner: SpreadsheetCleaner):
		self._file_name: str = file
		
		self._dataset: pd.DataFrame = None
		self._randomized_dataset: pd.DataFrame = None
		self._reader = reader
		self._cleaner = cleaner
	
	def is_dataset_set(self):
		""" Checks if dataset attribute is set """
		return True if self._dataset is not None else False

	def get_percentage(self, percent: float) -> int:
		""" Counts the total values and returns the number of items given a percentage """
		total_values = len(self._dataset)
		return int(total_values*percent)
	
	def clean_data(self):
		""" Does a cleansing process in the whole dataframe """

		print('Dataframe is being cleansed')
		self._dataset = self._cleaner.clean(self._dataset)

	def randomize_dataset(self):
		""" Uses dataset to generate a randomized one """
		column_names = list(self._dataset)
		numpy_dataset = self._dataset.to_numpy()
		np.random.shuffle(numpy_dataset)
		self._randomized_dataset = pd.DataFrame(numpy_dataset, columns=column_names)

	def read(self):
		""" Reads excel file and parses dataframe for retrieving methods """
		
		self._dataset = self.__reader.read_file(self._file_name)

		# probably this is redundant
		if self.is_dataset_set() is not True: 
			SpreadsheetNotSetError()
		
		self.clean_data()
		
	def retrieve_test_set(self) -> pd.DataFrame:
		""" Returns the 30% of the randomized parsed dataset """	
		self.randomize_dataset()	
		number_of_values = self.get_percentage(0.30)

		test_set = self._randomized_dataset[:number_of_values].copy()

		return test_set

	def retrieve_training_set(self) -> pd.DataFrame:
		""" Returns the 70% of the randomized parsed dataset """
		self.randomize_dataset()
		number_of_values = self.get_percentage(0.70)

		training_set = self._randomized_dataset[:number_of_values].copy()

		return training_set