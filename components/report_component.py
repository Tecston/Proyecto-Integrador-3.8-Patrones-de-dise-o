# components/report_component.py
from abc import ABC, abstractmethod
from typing import List


class ReportComponent(ABC):
    """Componente base del patrón Composite"""

    @abstractmethod
    def render(self) -> str: ...
