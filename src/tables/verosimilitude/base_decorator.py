from .interface import VerosimilitudeTable


class BaseVerosimilitudeTableDecorator(VerosimilitudeTable):
    
    def __init__(self, vt: VerosimilitudeTable):
        self._decorated: VerosimilitudeTable = vt

    # TODO: if we define a common method for all decorators, those are in here

    def retrieve(self):
        pass
