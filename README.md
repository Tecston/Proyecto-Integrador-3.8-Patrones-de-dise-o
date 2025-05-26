# 🧾 Generador de Reportes PDF desde CSV

Este proyecto permite generar reportes PDF automáticamente a partir de un archivo CSV, utilizando **Streamlit** como interfaz de usuario y **ReportLab** para el diseño de los reportes.

---

## 🚀 Características

- ✅ Subida de archivos CSV (hasta 200MB).
- ✅ Generación automática de reportes PDF con formato personalizado.
- ✅ Interfaz web simple y rápida con Streamlit.
- ✅ Soporte para múltiples campos de entrada desde el CSV.

---

## 🧱 Arquitectura del Proyecto

La siguiente estructura refleja cómo está organizado el código del generador de reportes PDF:

```text
📦 Proyecto-Integrador-3.8-Patrones-de-dise-o
├── 📂 builder/
│   ├── builder_interface.py       # Interfaz que define los pasos del builder
│   ├── pdf_report_builder.py      # Implementación concreta del builder en formato PDF
│   └── director.py                # Director que coordina el proceso de construcción
│
├── 📂 components/
│   ├── section.py                 # Define secciones del reporte
│   ├── text.py                    # Componente para texto simple
│   └── report_components.py       # Conjunto de componentes reutilizables
│
├── 📂 generator/
│   └── detailed_report.py         # Clase que instancia builder y director para generar el reporte
│
├── 📂 docs/
│   └── USAGE.csv                  # Archivo CSV de ejemplo para generar reportes
│
├── 📄 app.py                      # Punto de entrada principal de la aplicación con Streamlit
├── 📄 requirements.txt            # Dependencias del proyecto
└── 📄 README.md                   # Documentación del proyecto

---

## ⚙️ Requisitos

| Recurso     | Versión mínima | Notas                              |
|-------------|----------------|------------------------------------|
| Python      | 3.9            | Probado en 3.9 – 3.12              |
| pip         | 23.x           | Gestor de paquetes de Python       |
| Streamlit   | 1.34           | Ya viene en `requirements.txt`     |
| ReportLab   | 4.x            | Usado para generar el PDF          |


---

## 🛠️ Instalación

```bash
git clone https://github.com/TU-USUARIO/Proyecto-Integrador-3.8-Patrones-de-dise-o.git
cd Proyecto-Integrador-3.8-Patrones-de-dise-o

# Crear y activar entorno virtual (Windows PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
