from .table import VerisimilitudeTable


class BaseVerisimilitudeTable(VerisimilitudeTable):
    def has_zero_frequency(self):
        return self._zero_frequency_problem
