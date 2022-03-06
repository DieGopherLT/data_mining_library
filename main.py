from src.coordinator import MachineLearningCoordinator

from src.algorithms.zero_r.spreadsheet import ZeroRSpreadsheet
from src.algorithms.zero_r.trainer import ZeroRTrainer
from src.algorithms.zero_r.tester import ZeroRTester


def main():
    algorithm = int(input('Select algorithm\n1. Zero-R\n2. One-R\nOption: '))
    iterations = int(input('\nDefine number of iterations for testing: '))
    file_name = input('\nInsert file name: ')

    director = MachineLearningCoordinator(iterations)

    if algorithm == 1:
        target_column = input('\nInsert target column: ')
        spreadsheet = ZeroRSpreadsheet(f'data/{file_name}')
        spreadsheet.set_target_column(target_column)

        director.set_spreadsheet(spreadsheet)
        director.set_trainer(ZeroRTrainer())
        director.set_tester(ZeroRTester())

        print(director.execute_algorithm())

main()