# app.py
import streamlit as st
import tempfile
from generator.detailed_report import DetailedReport
from data.csv_adapter import CSVAdapter

st.set_page_config(page_title="Generador de Reportes PDF", page_icon="📝")

st.title("📝 Generador de Reportes PDF desde CSV")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Guardamos en archivo temporal para pasarlo al adapter
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    st.success("Archivo cargado correctamente. Generando reporte...")

    # Usamos Adapter + Template + Builder
    data_source = CSVAdapter(tmp_path)
    report = DetailedReport(data_source)
    pdf_bytes = report.generate()

    st.download_button(
        label="📥 Descargar PDF",
        data=pdf_bytes,
        file_name="reporte.pdf",
        mime="application/pdf",
    )
