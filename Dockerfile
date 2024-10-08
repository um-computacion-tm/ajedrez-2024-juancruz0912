FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-juancruz0912

WORKDIR /ajedrez-2024-juancruz0912

RUN pip install -r requirements.txt

# Ejecutar los tests y generar el reporte de coverage y guardarlos en un .txt
RUN coverage run -m unittest && coverage report -m > coverage_report.txt

# Usar un script de shell inline para mostrar el reporte y luego ejecutar el juego
CMD sh -c "cat coverage_report.txt && echo '\n--- Iniciando el juego ---\n' && python -m Juego.main"