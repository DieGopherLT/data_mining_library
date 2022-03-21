from ..base_decorator import BaseVerosimilitudeTableDecorator
from ..interface import VerosimilitudeTable


class ZeroFrequencyVerosimilitudeTable(BaseVerosimilitudeTableDecorator):

    def __init__(self, vt: VerosimilitudeTable):
        super().__init__(vt)

    # TODO: methods to transform a 'VerosimilitudeTable' into a one without zero frequencies

    def retrieve(self):
        pass
