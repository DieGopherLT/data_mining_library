import pandas as pd

class SpreadsheetReader():
	""" Returns a dataset file in pandas dataframe 
		by knowing it's file extension	
	"""
	def read_file(self, file: str):
		file_extension = file.split('.')[-1]
		read_function = None

		if file_extension == 'csv':
			read_function = pd.read_csv
		if file_extension == 'xlsx':
			read_function = pd.read_excel

		return read_function(file)

#dataset = SpreadsheetReader().read_file('Data.xlsx')