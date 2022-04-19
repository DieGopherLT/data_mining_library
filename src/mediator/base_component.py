from .interface import MachineLearningMediator


class MediableComponent:

    def __init__(self, mediator: MachineLearningMediator = None):
        self.mediator = mediator

    def set_mediator(self, mediator: MachineLearningMediator):
        self.mediator = mediator
