import pandas as pd
from src.coordinators.trainable_algorithms.trainer.interface import Trainer
from src.tables.frequency import FrequencyTableGenerator
from src.tables.verosimilitude.base import BaseVerosimilitudeTable
from src.tables.verosimilitude.concrete_decorators.zero_frequency import ZeroFrequencyVerosimilitudeTable
from pprint import pprint


class NaiveBayesTrainer(Trainer):

    def __init__(self, target_column: str, frequency_table_generator: FrequencyTableGenerator):
        self.__frequency_table_generator = frequency_table_generator
        self.__target_column = target_column

        self.__verosimilitude_tables = list()
        self.__avgs_and_stdevps = list()
        self.__model_description = dict()

    # 1. Calculate frequency tables
    # 2. Calculate verosimilitude tables
        # 2.1 If zero frequency, recalculate adding 1 to all elements
    # 3. Calculate avgs and stdevps
    # 4. Calculate posterior probabilities (tester)
    def train(self, spreadsheet: pd.DataFrame):
        self.__generate_verosimilitude_tables(spreadsheet)
        self.__generate_avgs_and_stdevps(spreadsheet)

    def __generate_verosimilitude_tables(self, spreadsheet: pd.DataFrame):
        categorical_attributes = spreadsheet.select_dtypes(include=['object'])
        frequency_tables = self.__frequency_table_generator.generate(categorical_attributes)

        verosimilitude_tables = BaseVerosimilitudeTable(frequency_tables).create()
        if verosimilitude_tables.has_zero_frequency():
            verosimilitude_tables = ZeroFrequencyVerosimilitudeTable(verosimilitude_tables.get_frequencies()).create()
            self.__verosimilitude_tables = verosimilitude_tables

        self.__verosimilitude_tables = verosimilitude_tables

        for column in categorical_attributes.columns:
            if column == self.__target_column:
                continue
            self.__model_description[column] = self.__verosimilitude_tables.get_table_for(column)

    def __generate_avgs_and_stdevps(self, spreadsheet: pd.DataFrame):
        numeric_attributes = spreadsheet.select_dtypes(include=['number'])
        numeric_attributes[self.__target_column] = spreadsheet[self.__target_column]

        for column in numeric_attributes.columns:
            if column == self.__target_column:
                continue
            association = numeric_attributes[[column, self.__target_column]]
            avg = association.groupby(self.__target_column).mean().to_dict()
            std_devps = association.groupby(self.__target_column).std(ddof=0).to_dict()
            self.__model_description[column] = {}
            self.__model_description[column]['avg'] = list(avg.values())[0]
            self.__model_description[column]['std'] = list(std_devps.values())[0]

    def retrieve_model_description(self):
        return self.__model_description
