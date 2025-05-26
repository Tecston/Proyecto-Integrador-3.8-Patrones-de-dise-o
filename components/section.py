# components/section.py
from typing import List
from .report_component import ReportComponent


class Section(ReportComponent):
    def __init__(self, title: str) -> None:
        self.title = title
        self.children: List[ReportComponent] = []

    def add(self, component: ReportComponent) -> None:
        self.children.append(component)

    def render(self) -> str:
        contenido = f"\n## {self.title}\n"
        for child in self.children:
            contenido += child.render()
        return contenido
