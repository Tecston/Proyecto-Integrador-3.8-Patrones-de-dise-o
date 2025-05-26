# builder/builder_interface.py
from abc import ABC, abstractmethod
from io import BytesIO


class ReportBuilder(ABC):
    """Interfaz del patrón Builder"""

    def __init__(self) -> None:
        # Aquí acumularemos el resultado (PDF en memoria)
        self.buffer = BytesIO()

    @abstractmethod
    def add_title(self, title: str) -> None: ...
    @abstractmethod
    def add_section(self, title: str, body: str) -> None: ...
    @abstractmethod
    def add_summary(self, total: float) -> None: ...
    @abstractmethod
    def get_result(self) -> BytesIO: ...
