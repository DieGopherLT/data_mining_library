import pandas as pd
	
class SpreadsheetCleaner:

	def clean(self, dataframe: pd.DataFrame):
		""" Returns a cleaned dataset """
		dataframe = self.clean_whitespaces(dataframe)

		return dataframe

	def clean_whitespaces(self, dataframe: pd.DataFrame):
		columns = list(dataframe)
		df = dataframe.copy()

		for column in columns:
			df[column] = df[column].astype(str).apply(lambda attr: attr.strip())
		
		return df
