from ..one_r.spreadsheet import OneRSpreadsheet
from src.spreadsheet.reader import SpreadsheetReader
from src.spreadsheet.cleaner import SpreadsheetCleaner


class NaiveBayesSpreadsheet(OneRSpreadsheet):

    def __init__(self, file_name: str, reader: SpreadsheetReader, cleaner: SpreadsheetCleaner):
        super().__init__(file_name, reader, cleaner)
