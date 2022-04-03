from src.mediator.interface import MachineLearningMediator
from src.distance_calculator.interface import DistanceCalculator

from src.algorithms.k_means.centroid_selector import CentroidSelector
from src.algorithms.k_means.clusterer import Clusterer
from src.algorithms.k_means.error_calculator import ErrorCalculator

class KMeansCoordinator(MachineLearningMediator):
    
    def __init__(self, k: int, distance_calculator: DistanceCalculator):
        self._k = k
        self._distance_calculator = distance_calculator
        
        self._centroid_selector = CentroidSelector(self)
        self._clusterer = Clusterer(self)
        self._error_calculator = ErrorCalculator(self)
    
    # ToDO: plan events in order to make them not to bubble between them
    def notify(self, event: str):
        if event == "start":
            # start the algorithm selecting random centroids
            pass
        elif event == "selected random centroids":
            # starts clustering
            pass
        elif event == "clustered":
            # recalculates centroids
            pass
        elif event == "recalculated centroids":
            # re starts clustering
            # calculates error
            pass
        elif event == "increased error" or "decreased error":
            # recalculates centroids
            pass
        
    def execute_algorithm(self):
        self.notify("start")