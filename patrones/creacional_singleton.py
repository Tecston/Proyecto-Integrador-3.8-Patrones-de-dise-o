class ConfiguracionSistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.config = {"modo": "producción", "version": "1.0"}
        return cls._instancia
