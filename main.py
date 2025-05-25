from patrones.creacional_singleton import ConfiguracionSistema
from patrones.estructural_adapter import SistemaAntiguo, AdaptadorSistema
from patrones.comportamiento_strategy import CarritoCompras, PagoPaypal
from patrones.adicional_factory import DocumentFactory

print("=== Singleton ===")
config1 = ConfiguracionSistema()
config2 = ConfiguracionSistema()
print(config1 is config2)

print("\n=== Adapter ===")
adaptador = AdaptadorSistema(SistemaAntiguo())
print(adaptador.get_data())

print("\n=== Strategy ===")
carrito = CarritoCompras(PagoPaypal())
print(carrito.procesar_pago(100))

print("\n=== Factory ===")
factory = DocumentFactory()
doc = factory.crear_documento("html")
print(doc.render())
