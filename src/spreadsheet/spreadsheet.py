from abc import ABC, abstractmethod


class Spreadsheet(ABC):
    """ Reads the spreadsheet file """

    @abstractmethod
    def read(self):
        """ Reads spreadsheet and parses data """
        pass

    @abstractmethod
    def retrieve_test_set(self):
        """ Randomizes data and returns the 30% of the total dataset """
        pass

    @abstractmethod
    def retrieve_training_set(self):
        """ Randomizes data and returns the 70% of the total dataset """
        pass