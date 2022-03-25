import pandas as pd
	
class SpreadsheetCleaner:

	def clean(self, dataframe: pd.DataFrame):
		""" Returns a cleaned dataset """
		dataframe = self.clean_whitespaces(dataframe)
		dataframe = self.clean_column_names_whitespaces(dataframe)

		return dataframe

	def clean_column_names_whitespaces(self, df: pd.DataFrame):
		""" Cleans whitespaces in column names """
		df.copy()
		columns = df.columns
		
		for column in columns:
			cleaned_column = column.strip()
			df = df.rename(columns={ column : cleaned_column })	

		return df

	def clean_whitespaces(self, dataframe: pd.DataFrame):
		""" Cleans whitespaces in the whole dataset """
		columns = list(dataframe)
		df = dataframe.copy()

		for column in columns:
			df[column] = df[column].astype(str).apply(lambda attr: attr.strip())
		
		return df
