from ..table import VerisimilitudeTable


class ZeroFrequencyVerisimilitudeTable(VerisimilitudeTable):
    def create(self):
        self.__solve_zero_frequency()
        self._calculate_verisimilitude_denominators()
        self._generate()
        return self

    def __solve_zero_frequency(self):
        fqts_copy = self._frequency_tables.copy()
        for i in range(len(fqts_copy)):
            column_frequency_table = fqts_copy[i]
            column_name = list(column_frequency_table)[0]
            target_values_frequency_table = column_frequency_table[column_name].items()

            for [target_value, frequency_table] in target_values_frequency_table:
                for [column_value, frequency] in frequency_table.items():
                    column_frequency_table[column_name][target_value][column_value] = frequency + 1

        self._frequency_tables = fqts_copy
