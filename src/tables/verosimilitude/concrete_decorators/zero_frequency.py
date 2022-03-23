from ..table import VerosimilitudeTable


class ZeroFrequencyVerosimilitudeTable(VerosimilitudeTable):
    def create(self):
        # Crear metodo de resolver frecuencia cero
        super().__calculate_verosimilitude_denominators()
        super().__generate()
    # TODO: methods to transform a 'VerosimilitudeTable' into a one without zero frequencies


