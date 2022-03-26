from copy import deepcopy
from functools import reduce


class VerisimilitudeTable:
    def __init__(self, frequency_tables: list):
        self._frequency_tables = frequency_tables
        self._verisimilitude_tables = list()
        self._zero_frequency_problem = bool
        self._verisimilitude_denominators = list()

    def create(self):
        self._calculate_verisimilitude_denominators()
        self._generate()
        return self

    def _calculate_verisimilitude_denominators(self):
        denominators = list()
        fqts_copy = self._frequency_tables.copy()
        for clmn_fqcy in fqts_copy:
            attribute_collection = dict()
            for [column, tbl_fqcy] in clmn_fqcy.items():
                attribute_numbers = dict()
                for [target_values, column_values] in tbl_fqcy.items():
                    attribute_numbers[target_values] = reduce(lambda x, y: x + y, column_values.values())

                attribute_collection[column] = attribute_numbers

            denominators.append(attribute_collection)

        self._verisimilitude_denominators = denominators

    def _generate(self):
        fqts_copy = deepcopy(self._frequency_tables)

        for i in range(len(fqts_copy)):
            column_frequency_table = fqts_copy[i]
            column_name = list(column_frequency_table)[0]
            target_values_frequency_table = column_frequency_table[column_name].items()

            for [target_value, frequency_table] in target_values_frequency_table:
                for [column_value, frequency] in frequency_table.items():
                    if frequency == 0:
                        self._zero_frequency_problem = True
                    verisimilitude = self.__calculate_verisimilitude(
                        frequency, self._verisimilitude_denominators[i][column_name][target_value])

                    column_frequency_table[column_name][target_value][column_value] = verisimilitude

        self._verisimilitude_tables = fqts_copy

    @staticmethod
    def __calculate_verisimilitude(numerator: int, denominator: int):
        return float(numerator) / float(denominator)

    def get_frequencies(self):
        return self._frequency_tables

    def get_table(self):
        return self._verisimilitude_tables

    def get_table_for(self, column: str):
        for table in self._verisimilitude_tables:
            if table.get(column) is not None:
                return list(table.values())[0]
        return None
