import pandas as pd
from src.coordinators.trainable_algorithms.trainer.interface import Trainer
from src.tables.frequency import FrequencyTableGenerator
from src.tables.verosimilitude.base import BaseVerosimilitudeTable
from src.tables.verosimilitude.concrete_decorators.zero_frequency import ZeroFrequencyVerosimilitudeTable


class NaiveBayesTrainer(Trainer):

    def __init__(self, target_column: str, frequency_table_generator: FrequencyTableGenerator):
        self.__frequency_table_generator = frequency_table_generator
        self.__target_column = target_column

        self.__categoric_attributes: pd.DataFrame = None
        self.__numeric_attributes: pd.DataFrame = None
        # self.__frequency_tables = list() // I think it is unnecessary
        self.__verosimilitude_tables = list()
        self.__avgs_and_stdevps = list()
        self.__model_description = dict()

    # 1. Calculate frequency tables
    # 2. Calculate verosimilitude tables
        # 2.1 If zero frequency, recalculate adding 1 to all elements
    # 3. Calculate avgs and stdevps
    # 4. Calculate posterior probabilities (tester)
    def train(self, spreadsheet: pd.DataFrame):
        # self.__generate_similitude_tables(spreadsheet)
        self.__generate_avgs_and_stdevps(spreadsheet)

    def __generate_similitude_tables(self, spreadsheet: pd.DataFrame):
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

        frequency_tables = self.__frequency_table_generator.generate(numeric_attributes)

        # ToDo: find out why petal length is unrecognized
        # for fqt in frequency_tables:
        #     numerical_attr_df = pd.DataFrame(fqt)
        #     for column in numeric_attributes.columns:
        #         if column == self.__target_column:
        #             continue
        #         print(column)
        #         pprint(numerical_attr_df[column])

    def retrieve_model_description(self):
        return self.__model_description
