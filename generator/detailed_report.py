# generator/detailed_report.py
from typing import List, Dict
from io import BytesIO
from data.data_source import DataSource
from builder.pdf_report_builder import PDFReportBuilder
from builder.director import ReportDirector
from .base_report_generator import BaseReportGenerator


class DetailedReport(BaseReportGenerator):
    """Implementa el Template Method utilizando nuestro PDFBuilder"""

    def __init__(self, data_source: DataSource) -> None:
        self.data_source = data_source

    # --------- métodos concretos ------------
    def _get_data(self) -> List[Dict[str, str]]:
        return self.data_source.get_data()

    def _build_document(self, data: List[Dict[str, str]]) -> BytesIO:
        builder = PDFReportBuilder()
        director = ReportDirector(builder)
        director.build_report(data)
        return builder.get_result()
