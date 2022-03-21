from abc import ABC, abstractmethod


class Tester(ABC):

    @abstractmethod
    def test(self, model_description, test_set):
        pass

    @abstractmethod
    def retrieve_test_output(self):
        pass
