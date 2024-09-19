FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-juancruz0912

WORKDIR /ajedrez-2024-juancruz0912

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python3 -m Juego.main"]

# docker buildx build -t ajedrez /ruta/al/directorio
# docker run -i ajedrez