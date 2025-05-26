# data/csv_adapter.py
import csv
from typing import List, Dict
from .data_source import DataSource


class CSVAdapter(DataSource):
    """Lee un archivo CSV y lo adapta a la interfaz DataSource"""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_data(self) -> List[Dict[str, str]]:
        with open(self.file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
