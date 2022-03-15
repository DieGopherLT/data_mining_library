from enum import Enum

from src.selectors.file.explorer import FileExplorer

from src.coordinator import MachineLearningCoordinator

from src.algorithms.zero_r.spreadsheet import ZeroRSpreadsheet
from src.algorithms.zero_r.trainer import ZeroRTrainer
from src.algorithms.zero_r.tester import ZeroRTester

from src.algorithms.one_r.spreadsheet import OneRSpreadsheet
from src.algorithms.one_r.trainer import OneRTrainer
from src.algorithms.one_r.tester import OneRTester

from src.spreadsheet.cleaner import SpreadsheetCleaner
from src.spreadsheet.reader import SpreadsheetReader


class Algorithms(Enum):
    ZeroR = 1
    OneR = 2
    NaiveBayes = 3


def main():
    algorithm = int(input('Select algorithm\n1. Zero-R\n2. One-R\nOption: '))
    iterations = int(input('\nDefine number of iterations for testing: '))
    file_name = FileExplorer().select_file_in('data/')

    director = MachineLearningCoordinator(iterations)

    if algorithm == Algorithms.ZeroR.value:
        target_column = input('\nInsert target column: ')

        spreadsheet = ZeroRSpreadsheet(file_name, SpreadsheetReader(), SpreadsheetCleaner())
        spreadsheet.set_target_column(target_column)

        director.set_spreadsheet(spreadsheet)
        director.set_trainer(ZeroRTrainer())
        director.set_tester(ZeroRTester())

        print(director.execute_algorithm())

    elif algorithm == Algorithms.OneR.value:
        target_column = input('\nInsert target column: ')

        spreadsheet = OneRSpreadsheet(file_name, SpreadsheetReader(), SpreadsheetCleaner())

        director.set_spreadsheet(spreadsheet)
        director.set_trainer(OneRTrainer(target_column))
        director.set_tester(OneRTester())

        print(director.execute_algorithm())

    elif algorithm == Algorithms.NaiveBayes.value:
        print('\nAlgun dia...')


main()
