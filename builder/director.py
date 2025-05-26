from typing import List, Dict
from .builder_interface import ReportBuilder

class ReportDirector:
    """Orquesta los pasos del builder (Director del patrón)"""

    def __init__(self, builder: ReportBuilder) -> None:
        self.builder = builder

    def build_report(self, data: List[Dict[str, str]]) -> None:
        self.builder.add_title("Reporte de Ventas")

        for fila in data:
            producto = fila.get("producto", "Producto sin nombre")
            cantidad = float(fila.get("cantidad", 0))
            precio = float(fila.get("precio", 0))
            monto = cantidad * precio

            self.builder.add_section(
                title=producto,
                body=f"Monto: ${monto:,.2f}"
            )

        total = sum(
            float(fila.get("cantidad", 0)) * float(fila.get("precio", 0))
            for fila in data
        )
        self.builder.add_summary(total)
