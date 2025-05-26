# components/text.py
from .report_component import ReportComponent


class Text(ReportComponent):
    def __init__(self, texto: str) -> None:
        self.texto = texto

    def render(self) -> str:
        return f"{self.texto}\n"
