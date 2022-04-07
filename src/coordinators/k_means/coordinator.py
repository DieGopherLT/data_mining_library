import pandas as pd

from src.mediator.interface import MachineLearningMediator
from src.mediator.base_component import MediableComponent

# from src.distance_calculator.interface import DistanceCalculator

from src.algorithms.k_means.centroid_selector import CentroidSelector
from src.algorithms.k_means.clusterer import Clusterer
from src.algorithms.k_means.error_calculator import ErrorCalculator


class KMeansCoordinator(MachineLearningMediator):

    def __init__(self, dataset: pd.DataFrame):
        self._k = 0
        self._r = 0
        # self._categorical_distance_calculator = None
        # self._numeric_distance_calculator = None
        self._dataset = dataset

        self._centroid_selector = CentroidSelector(self, dataset)
        self._clusterer = Clusterer(self, dataset)
        self._error_calculator = ErrorCalculator(self)

    def set_k(self, k: int):
        self._k = k

    def set_r(self, r):
        self._r = r

    # def set_distance_calculator(self, categorical_calculator: DistanceCalculator, numeric_calculator: DistanceCalculator):
    #     self._categorical_distance_calculator = categorical_calculator
    #     self._numeric_distance_calculator = numeric_calculator

    # ToDO: plan events in order to make them not to bubble between them
    def notify(self, sender: MediableComponent, event: str):
        if event == "start":
            # start the algorithm selecting random centroids
            self._centroid_selector.select_random(self._k)
        elif sender == self._centroid_selector and event == "selected_random_centroids":
            # starts clustering
            dataframe_with_removed_centroids = \
                self._dataset.copy()\
                .drop(self._centroid_selector.retrieve_random_centroids().index)
            dataframe_with_restored_indexed = dataframe_with_removed_centroids.reset_index(drop=True)
            # call clusterer method to cluster passing centroids, dataset without centroids and distance calculator
        elif sender == self._clusterer and event == "clustered":
            # recalculates centroids
            pass
        elif self._centroid_selector and event == "recalculated_centroids":
            # re starts clustering
            # calculates error
            pass
        elif event == "increased error" or "decreased error":
            # recalculates centroids
            pass

    def execute_algorithm(self):
        self.notify(None, "start")
