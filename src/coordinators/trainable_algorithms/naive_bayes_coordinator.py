from src.spreadsheet import spreadsheet
from .trainer.interface import Trainer
from .tester.interface import Tester
from .coordinator import TrainableAlgorithmsCoordinator

from pprint import pprint


class NaiveBayesCoordinator(TrainableAlgorithmsCoordinator):
    """ Coordinates spreadsheet, trainer and tester classes to execute a machine learning algorithm """

    def execute_algorithm(self):
        if not self._is_algorithm_set():
            return 'No algorithm set'

        self._spreadsheet.read()

        for _ in range(self._test_iterations):
            training_set = self._spreadsheet.retrieve_training_set()

            self._trainer.train(training_set)
            model_description = self._trainer.retrieve_model_description()
            #pprint(model_description)

            test_set = self._spreadsheet.retrieve_test_set()
            self._tester.test(model_description, test_set)

        return self._tester.retrieve_test_output()
