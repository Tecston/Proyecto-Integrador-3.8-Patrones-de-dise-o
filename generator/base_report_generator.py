# generator/base_report_generator.py
from abc import ABC, abstractmethod
from typing import List, Dict
from io import BytesIO


class BaseReportGenerator(ABC):
    """Template Method"""

    def generate(self) -> BytesIO:
        # Paso 1: obtener datos
        data = self._get_data()

        # Paso 2: construir el documento (Builder dentro)
        resultado = self._build_document(data)

        return resultado

    # ----------- hooks a implementar -----------
    @abstractmethod
    def _get_data(self) -> List[Dict[str, str]]: ...
    @abstractmethod
    def _build_document(self, data: List[Dict[str, str]]) -> BytesIO: ...
