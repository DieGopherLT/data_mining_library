import os
from .exception import FileExplorerDirectoryError

class FileExplorer:
	def __get_files(self, directory: str) -> str:	
		return os.listdir(directory)

	def __is_directory(self, directory) -> bool:
		return os.path.isdir(directory) 

	def __print_file_preview(self, files):
		for i in range(len(files)):
			print(f'[{i+1}] {files[i]}')

	def select_file_in(self, directory: str) -> str:
		if not self.__is_directory(directory):

			FileExplorerDirectoryError(directory)

		files = self.__get_files(directory)

		print('Select a file: \n')

		self.__print_file_preview(files)

		file_index = int(input('Enter file index: '))	
		file_name = files[file_index-1]

		return f'{directory}{file_name}'