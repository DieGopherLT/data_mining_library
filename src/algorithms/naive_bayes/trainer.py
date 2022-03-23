import pandas as pd
from src.coordinators.trainable_algorithms.trainer.interface import Trainer
from src.tables.frequency import FrequencyTableGenerator
from src.tables.verosimilitude.base import BaseVerosimilitudeTable
from src.tables.verosimilitude.concrete_decorators.zero_frequency import ZeroFrequencyVerosimilitudeTable


class NaiveBayesTrainer(Trainer):
    
    def __init__(self, frequency_table_generator):
        self.__frequency_table_generator: FrequencyTableGenerator = frequency_table_generator

        self.__categoric_attributes = None
        self.__numeric_attributes = None
        self.__frequency_tables = list()
        self.__verosimilitude_tables = list()
        self.__avgs_and_stdevps = list()
        self.__model_description = None

    # 1. Calculate frequency tables
    # 2. Calculate verosimilitude tables
        # 2.1 If zero frequency, recalculate adding 1 to all elements
    # 3. Calculate avgs and stdevps
    # 4. Calculate posterior probabilities (tester)
    def train(self, spreadsheet: pd.DataFrame):
        self.__categoric_attributes = spreadsheet.select_dtypes(include=['object'])
        self.__numeric_attributes = spreadsheet.select_dtypes(include=['number'])

        self.__frequency_tables = self.__frequency_table_generator.generate(self.__categoric_attributes)

        verosimilitude_tables = BaseVerosimilitudeTable(self.__frequency_tables).create()
        if verosimilitude_tables.has_zero_frequency():
            verosimilitude_tables = ZeroFrequencyVerosimilitudeTable(verosimilitude_tables.get_frequencies()).create()

    def retrieve_model_description(self):
        pass
