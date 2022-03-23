from .table import VerosimilitudeTable


class BaseVerosimilitudeTable(VerosimilitudeTable):
    def has_zero_frequency(self):
        return super()._zero_frequency_problem
