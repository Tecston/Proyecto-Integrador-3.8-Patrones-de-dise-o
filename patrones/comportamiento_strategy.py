from abc import ABC, abstractmethod

class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class PagoPaypal(EstrategiaPago):
    def pagar(self, monto):
        return f"Pagando {monto} con PayPal"

class PagoTarjeta(EstrategiaPago):
    def pagar(self, monto):
        return f"Pagando {monto} con Tarjeta"

class CarritoCompras:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def procesar_pago(self, monto):
        return self.estrategia.pagar(monto)
