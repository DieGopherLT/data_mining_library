class FileExplorerError(Exception):
	def __init__(self, message):
		super().__init__(message)
	
class FileExplorerDirectoryError():
	def __init__(self, path):
		raise FileExplorerError(f'{path} is not a directory')
	