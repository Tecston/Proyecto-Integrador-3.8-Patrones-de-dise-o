# builder/pdf_report_builder.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.units import cm
from typing import List
from .builder_interface import ReportBuilder


class PDFReportBuilder(ReportBuilder):
    """Builder concreto que genera un PDF en memoria"""

    def __init__(self) -> None:
        super().__init__()
        self.elements: List = []
        self.styles = getSampleStyleSheet()

    # ---------- pasos de construcción ----------
    def add_title(self, title: str) -> None:
        self.elements.append(Paragraph(title, self.styles["Title"]))
        self.elements.append(Spacer(1, 1 * cm))

    def add_section(self, title: str, body: str) -> None:
        self.elements.append(Paragraph(title, self.styles["Heading2"]))
        self.elements.append(Paragraph(body, self.styles["BodyText"]))
        self.elements.append(Spacer(1, .6 * cm))

    def add_summary(self, total: float) -> None:
        self.elements.append(Paragraph("Resumen", self.styles["Heading2"]))
        table = Table([["Total", f"${total:,.2f}"]],
                      hAlign="LEFT", colWidths=[4 * cm, 4 * cm])
        self.elements.append(table)

    # ---------- resultado ----------
    def get_result(self):
        doc = SimpleDocTemplate(self.buffer, pagesize=A4)
        doc.build(self.elements)
        self.buffer.seek(0)          # importante
        return self.buffer
