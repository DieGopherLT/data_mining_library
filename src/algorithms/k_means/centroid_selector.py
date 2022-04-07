import pandas as pd

from src.mediator.base_component import MediableComponent
from src.mediator.interface import MachineLearningMediator


class CentroidSelector(MediableComponent):

    def __init__(self, mediator: MachineLearningMediator, dataframe: pd.DataFrame):
        super().__init__(mediator)
        self._dataframe = dataframe
        self.__random_centroids = None

    def select_random(self, k: int):
        self.__random_centroids = self._dataframe.sample(n=k)
        self.mediator.notify(self, "selected_random_centroids")

    def retrieve_random_centroids(self):
        return self.__random_centroids
