import pandas as pd
import os.path
from .exception import SpreadsheetNotFoundError

class SpreadsheetReader():
	""" Returns a dataset file in pandas dataframe 
		by knowing it's file extension	
	"""
	def is_file_exists(self, file: str) -> bool:
		return True if os.path.exists(file) else False

	def read_file(self, file: str) -> pd.DataFrame:
		if not self.is_file_exists(file):
			SpreadsheetNotFoundError()

		file_extension = file.split('.')[-1]
		read_function = None

		if file_extension == 'csv':
			read_function = pd.read_csv
		if file_extension == 'xlsx':
			read_function = pd.read_excel

		return read_function(file)