from abc import ABC, abstractmethod


class Tester(ABC):
    """ Tests a given description model """

    @abstractmethod
    def test(self, model_description):
        """ Main test method """
        pass

    @abstractmethod
    def retrieve_test_output(self):
        """ Returns test results """
        pass