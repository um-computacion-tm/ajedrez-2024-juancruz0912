FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-juancruz0912

WORKDIR /ajedrez-2024-juancruz0912

RUN pip install -r requirements.txt

# Crear un script de shell para ejecutar los comandos y hacer depuración
RUN echo '#!/bin/sh' > /run_tests_and_game.sh && \
    echo 'set -x' >> /run_tests_and_game.sh && \
    echo 'echo "Ejecutando tests con coverage..."' >> /run_tests_and_game.sh && \
    echo 'coverage run -m unittest' >> /run_tests_and_game.sh && \
    echo 'echo "Generando reporte de coverage..."' >> /run_tests_and_game.sh && \
    echo 'coverage report -m' >> /run_tests_and_game.sh && \
    echo 'echo "Contenido del directorio actual:"' >> /run_tests_and_game.sh && \
    echo 'ls -la' >> /run_tests_and_game.sh && \
    echo 'echo "Contenido del archivo .coverage (si existe):"' >> /run_tests_and_game.sh && \
    echo 'cat .coverage || echo "Archivo .coverage no encontrado"' >> /run_tests_and_game.sh && \
    echo 'echo "Iniciando el juego..."' >> /run_tests_and_game.sh && \
    echo 'python -m Juego.main' >> /run_tests_and_game.sh && \
    chmod +x /run_tests_and_game.sh

CMD ["/run_tests_and_game.sh"]