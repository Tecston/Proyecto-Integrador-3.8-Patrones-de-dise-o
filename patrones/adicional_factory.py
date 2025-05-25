from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def render(self):
        pass

class PDF(Documento):
    def render(self):
        return "Documento PDF generado"

class HTML(Documento):
    def render(self):
        return "Documento HTML generado"

class DocumentFactory:
    def crear_documento(self, tipo):
        if tipo == "pdf":
            return PDF()
        elif tipo == "html":
            return HTML()
