from .interface import VerosimilitudeTable


class BaseVerosimilitudeTable(VerosimilitudeTable):

    def __init__(self, frequency_table: list):
        self._dataframe = frequency_table

        self._verosimilitude_table = None

    # TODO: make all methods to transform frequency table into verosimilitude table

    def retrieve(self):
        return self._verosimilitude_table
