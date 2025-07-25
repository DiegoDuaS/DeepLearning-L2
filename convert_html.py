import nbformat
from nbconvert import HTMLExporter

# Cargar notebook
with open("lab2-1.ipynb", "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Exportar a HTML
html_exporter = HTMLExporter()
html_data, _ = html_exporter.from_notebook_node(notebook)

# Guardar en archivo HTML
with open("lab2-1.html", "w", encoding="utf-8") as f:
    f.write(html_data)

print("Conversión completada: lab2-1.html")
