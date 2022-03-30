import pandas as pd

from ..one_r.spreadsheet import OneRSpreadsheet
from src.spreadsheet.reader import SpreadsheetReader
from src.spreadsheet.cleaner import SpreadsheetCleaner


class NaiveBayesSpreadsheet(OneRSpreadsheet):

    def __init__(self, file_name: str, reader: SpreadsheetReader, cleaner: SpreadsheetCleaner):
        super().__init__(file_name, reader, cleaner)
        # self.__test_percentage = test_percentage
        # self.__training_percentage = training_percentage

    def read(self):
        self._dataset = self._reader.read_file(self._file_name)

    def randomize_dataset(self):
        """ Uses dataset to generate a randomized one """
        self._randomized_dataset = self._dataset.sample(frac=1)

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
