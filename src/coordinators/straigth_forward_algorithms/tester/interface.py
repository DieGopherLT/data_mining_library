from abc import ABC, abstractmethod


class Tester(ABC):

    @abstractmethod
    def test(self, instance):
        pass

    @abstractmethod
    def retrieve_test_output(self):
        pass
