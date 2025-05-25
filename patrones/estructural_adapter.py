class SistemaAntiguo:
    def obtener_datos(self):
        return "Datos en formato antiguo"

class AdaptadorSistema:
    def __init__(self, sistema):
        self.sistema = sistema

    def get_data(self):
        return self.sistema.obtener_datos()
