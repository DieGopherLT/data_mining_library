from functools import reduce


class VerosimilitudeTable:
    def __init__(self, frequency_tables: list):
        self._frequency_tables = frequency_tables
        self._verosimilitude_table = None
        self._verosimilitude_denominators = list()

    def __calculate_verosimilitude_denominators(self):
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

        self._verosimilitude_denominators = denominators

    def __generate(self):
        for i in range(len(self._frequency_tables)):
            column_frequency_table = self._frequency_tables[i]
            column_name = list(column_frequency_table)[0]
            target_values_frequency_table = column_frequency_table[column_name].items()

            for [target_value, frequency_table] in target_values_frequency_table:
                for [column_value, frequency] in frequency_table.items():
                    verosimilitude = self.__calculate_verosimilitude(
                        frequency, self._verosimilitude_denominators[i][column_name][target_value])
                    column_frequency_table[column_name][target_value][column_value] = verosimilitude

    @staticmethod
    def __calculate_verosimilitude(numerator: int, denominator: int):
        return numerator / denominator
