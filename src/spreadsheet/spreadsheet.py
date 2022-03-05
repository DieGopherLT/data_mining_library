from abc import ABC, abstractmethod


class Spreadsheet(ABC):
    """ Reads the spreadsheet file """

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def retrieve_data(self):
        """ Returns data formatted according to the algorithm to be used """
        pass
