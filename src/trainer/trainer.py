from abc import ABC, abstractmethod


class Trainer(ABC):
    """ From data coming from spreadsheet, will create the description model """

    @abstractmethod
    def train(self, spreadsheet):
        """ Creates a data model description """
        pass

    @abstractmethod
    def retrieve_model_description(self):
        """ Returns model description """
        pass
