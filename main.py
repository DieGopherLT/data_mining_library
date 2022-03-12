from enum import Enum

from src.coordinator import MachineLearningCoordinator

from src.algorithms.zero_r.spreadsheet import ZeroRSpreadsheet
from src.algorithms.zero_r.trainer import ZeroRTrainer
from src.algorithms.zero_r.tester import ZeroRTester

from src.spreadsheet.cleaner import SpreadsheetCleaner
from src.spreadsheet.reader import SpreadsheetReader

class Algorithms(Enum):
    ZeroR = 1
    OneR = 2
    NaiveBayes = 3


def main():
    algorithm = int(input('Select algorithm\n1. Zero-R\n2. One-R\nOption: '))
    iterations = int(input('\nDefine number of iterations for testing: '))
    file_name = input('\nInsert file name: ')

    director = MachineLearningCoordinator(iterations)

    match algorithm:
        case Algorithms.ZeroR.value:
            target_column = input('\nInsert target column: ')
            spreadsheet = ZeroRSpreadsheet(f'data/{file_name}', SpreadsheetReader(), SpreadsheetCleaner())
            spreadsheet.set_target_column(target_column)

            director.set_spreadsheet(spreadsheet)
            director.set_trainer(ZeroRTrainer())
            director.set_tester(ZeroRTester())

            print(director.execute_algorithm())
            
        case Algorithms.OneR.value:
            print('\nEl Lunes sin falta carnal')
            
        case Algorithms.NaiveBayes.value:
            print('\nAlgun dia...')

main()