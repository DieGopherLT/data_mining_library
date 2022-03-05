from spreadsheet import spreadsheet
from trainer import trainer
from tester import tester


class MachineLearningCoordinator:
    """ Coordinates spreadsheet, trainer and tester classes to execute a machine learning algorithm """

    def __init__(self, test_iterations: int):
        self._spreadsheet: spreadsheet.Spreadsheet = None
        self._trainer: trainer.Trainer = None
        self._tester: tester.Tester = None
        self._test_iterations: int = test_iterations
        self._results = list()

    def set_spreadsheet(self, ss: spreadsheet.Spreadsheet) -> None:
        self._spreadsheet = ss

    def set_trainer(self, tr: trainer.Trainer) -> None:
        self._trainer = tr

    def set_tester(self, tst: tester.Tester) -> None:
        self._tester = tst

    def execute_algorithm(self):
        def is_algorithm_set():
            if type(self._spreadsheet) is None:
                return False
            if type(self._trainer) is None:
                return False
            if type(self._tester) is None:
                return False
            return True

        if not is_algorithm_set():
            return 'No algorithm set'

        self._spreadsheet.read()
        training_set = self._spreadsheet.retrieve_training_set()

        self._trainer.train(training_set)
        model_description = self._trainer.retrieve_model_description()

        for _ in range(self._test_iterations):
            test_set = self._spreadsheet.retrieve_test_set()
            self._tester.test(model_description, test_set)

            result = self._tester.retrieve_test_output()
            self._results.append(result)

        return self._results
