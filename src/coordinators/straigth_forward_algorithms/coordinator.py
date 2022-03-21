from src.spreadsheet.spreadsheet import Spreadsheet
from .tester.interface import Tester


class StraightForwardAlgorithmsCoordinator:

    def __init__(self):
        self._spreadsheet = None
        self._tester = None

    def set_spreadsheet(self, spreadsheet: Spreadsheet):
        self._spreadsheet = spreadsheet
        
    def set_tester(self, tester: Tester):
        self._tester = tester

    def execute_algorithm(self):
        pass
