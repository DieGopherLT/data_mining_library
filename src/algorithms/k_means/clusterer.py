import pandas as pd

from src.mediator.interface import MachineLearningMediator
from src.mediator.base_component import MediableComponent

from src.distance_calculator.interface import DistanceCalculator


class Clusterer(MediableComponent):

    def __init__(self, mediator: MachineLearningMediator, dataset: pd.DataFrame):
        super().__init__(mediator)
        self._dataset = dataset

    def cluster(self, centroids: pd.DataFrame, dataset: pd.DataFrame):
        pass