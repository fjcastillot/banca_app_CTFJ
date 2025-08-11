from abc import ABC, asbtracmethod

class BaseCredito(ABC):
    def __init__(self, monto, plazo, tasa):
        self.monto = monto
        self.plazo = plazo
        self.tasa = tasa

        @asbtracmethod
        def calcular_cuota(self):
            pass