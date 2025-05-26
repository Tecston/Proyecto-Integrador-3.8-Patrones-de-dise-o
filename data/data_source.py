# data/data_source.py
from abc import ABC, abstractmethod
from typing import List, Dict


class DataSource(ABC):
    """Interfaz del patrón Adapter"""

    @abstractmethod
    def get_data(self) -> List[Dict[str, str]]: ...
