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
