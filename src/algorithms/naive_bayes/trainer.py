import pandas as pd
from functools import reduce

from src.coordinators.trainable_algorithms.trainer.interface import Trainer
from src.tables.frequency import FrequencyTableGenerator
from src.tables.verisimilitude.base import BaseVerisimilitudeTable
from src.tables.verisimilitude.concrete_decorators.zero_frequency import ZeroFrequencyVerisimilitudeTable

class NaiveBayesTrainer(Trainer):

    def __init__(self, target_column: str, frequency_table_generator: FrequencyTableGenerator):
        self.__frequency_table_generator = frequency_table_generator
        self.__target_column = target_column

        self.__verisimilitude_tables = list()
        self.__avgs_and_stdevps = list()
        self.__model_description = dict()

    def train(self, spreadsheet: pd.DataFrame):
        self.__generate_verisimilitude_tables(spreadsheet)
        self.__calculate_avgs_and_stdevps(spreadsheet)
        self.__calculate_target_column_verisimilitude(spreadsheet)

    def __generate_verisimilitude_tables(self, spreadsheet: pd.DataFrame):
        categorical_attributes = spreadsheet.select_dtypes(include=['object'])
        frequency_tables = self.__frequency_table_generator.generate(categorical_attributes)

        verisimilitude_tables = BaseVerisimilitudeTable(frequency_tables).create()
        if verisimilitude_tables.has_zero_frequency():
            verisimilitude_tables = ZeroFrequencyVerisimilitudeTable(verisimilitude_tables.get_frequencies()).create()
            self.__verisimilitude_tables = verisimilitude_tables

        self.__verisimilitude_tables = verisimilitude_tables

        for column in categorical_attributes.columns:
            if column == self.__target_column:
                continue
            self.__model_description[column] = self.__verisimilitude_tables.get_table_for(column)

    def __calculate_avgs_and_stdevps(self, spreadsheet: pd.DataFrame):
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

    def __calculate_target_column_verisimilitude(self, spreadsheet: pd.DataFrame):
        frequencies = {}
        self.__model_description[self.__target_column] = {}

        attribute_values = spreadsheet[self.__target_column].unique()
        for attribute_value in attribute_values:
            attribute_count = spreadsheet[spreadsheet[self.__target_column] == attribute_value].count()[0]
            frequencies[attribute_value] = attribute_count

        frequency_sum = reduce(lambda x, y: x + y, frequencies.values())
        similitude = {key: value / frequency_sum for key, value in frequencies.items()}
        self.__model_description[self.__target_column] = similitude

    def retrieve_model_description(self):
        """
            Formally, Naive Bayes algorithm does not produce a model description, instead returns
            a group of processed data that functions as the result of calculating values that are
            conformed by:

            categoric attributes, which has:
                - Verisimilitude tables with regard to the target column values.

            numeric attributes:
                - Which are processed by calculating the average and standard deviations
                  with regard to the target column values.
        """
        return self.__model_description
