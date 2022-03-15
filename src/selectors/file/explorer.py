import os
from .exception import FileExplorerDirectoryError

class FileExplorer:
	def __get_files(self, directory: str) -> str:	
		return os.listdir(directory)

	def is_directory(self, directory) -> bool:
		return os.path.isdir(directory) 

	def select_file_in(self, directory: str) -> str:
		if not self.is_directory(directory):
			FileExplorerDirectoryError(directory)

		files = self.__get_files(directory)

		print('Select a file: \n')

		for i in range(len(files)):
			print(f'[{i+1}] {files[i]}')

		file_index = int(input('Enter file index: '))	
		file_name = files[file_index-1]

		return f'{directory}{file_name}'
