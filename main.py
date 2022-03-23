from enum import Enum

from src.selectors.file.explorer import FileExplorer
from src.selectors.target_column.selector import TargetColumnSelector

from src.coordinators.trainable_algorithms.coordinator import TrainableAlgorithmsCoordinator

from src.algorithms.zero_r.spreadsheet import ZeroRSpreadsheet
from src.algorithms.zero_r.trainer import ZeroRTrainer
from src.algorithms.zero_r.tester import ZeroRTester

from src.algorithms.one_r.spreadsheet import OneRSpreadsheet
from src.algorithms.one_r.trainer import OneRTrainer
from src.algorithms.one_r.tester import OneRTester

from src.spreadsheet.cleaner import SpreadsheetCleaner
from src.spreadsheet.reader import SpreadsheetReader

from src.tables.frequency import FrequencyTableWithZeros


class Algorithms(Enum):
    ZeroR = 1
    OneR = 2
    NaiveBayes = 3


def main():
    algorithm = int(input('Select algorithm\n1. Zero-R\n2. One-R\nOption: '))
    file_name = FileExplorer().select_file_in('data/')

    reader = SpreadsheetReader()

    if algorithm == Algorithms.ZeroR.value:
        iterations = int(input('\nDefine number of iterations for testing: '))
        director = TrainableAlgorithmsCoordinator(iterations)

        target_column = TargetColumnSelector(reader).select_target_column_in(file_name, 3)

        spreadsheet = ZeroRSpreadsheet(file_name, reader, SpreadsheetCleaner())
        spreadsheet.set_target_column(target_column)

        director.set_spreadsheet(spreadsheet)
        director.set_trainer(ZeroRTrainer())
        director.set_tester(ZeroRTester())

        print(director.execute_algorithm())

    elif algorithm == Algorithms.OneR.value:
        iterations = int(input('\nDefine number of iterations for testing: '))
        director = TrainableAlgorithmsCoordinator(iterations)

        target_column = TargetColumnSelector(reader).select_target_column_in(file_name, 3)

        spreadsheet = OneRSpreadsheet(file_name, reader, SpreadsheetCleaner())
        trainer = OneRTrainer(target_column, FrequencyTableWithZeros(target_column))

        director.set_spreadsheet(spreadsheet)
        director.set_trainer(trainer)
        director.set_tester(OneRTester())

        print(director.execute_algorithm())

    elif algorithm == Algorithms.NaiveBayes.value:
        print('\nAlgun dia...')


main()
