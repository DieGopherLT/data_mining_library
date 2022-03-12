class SpreadsheetError(Exception):
	def __init__(self,message):
		super().__init__(message)

class SpreadsheetNotFoundError():
	def __init__(self):
		raise SpreadsheetError('Spreadsheet file not found or file extension does not match .xlsx or .csv')

class SpreadsheetNotSetError():
	def __init__(self):
		raise SpreadsheetError('Spreadsheet is not set, cannot generate dataset')

class TargetColumnError():
	def __init__(self):
		raise SpreadsheetError('Target column is not set')

class TargetColumnNotFoundError():
	def __init__(self):
		raise SpreadsheetError('Target column not found in the column names of the dataset')
	
	