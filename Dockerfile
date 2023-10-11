FROM python:3.12.0-slim-bullseye
WORKDIR /app/src
COPY . /app/src/ 
# Copia el script de inicio al contenedor
COPY start.sh /start.sh
RUN  pip install -r requirements.txt && python -m venv venv && \
    . venv/bin/activate && \pip install --upgrade pip 
#ENTRYPOINT python3 index.py




# Ejecuta el script de inicio cuando se inicia el contenedor

