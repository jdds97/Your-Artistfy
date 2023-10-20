# Usamos una imagen de Ubuntu como base
FROM python:3.10.13-slim-bullseye

# Actualizamos el sistema y instalamos las dependencias necesarias
RUN apt-get update -y && \
    apt-get install -y \
    python3-pip

# Copiamos los archivos del proyecto al contenedor
COPY . /app

# Establecemos el directorio de trabajo
WORKDIR /app

# Instalamos las dependencias de Python
RUN pip3 install -r requirements.txt \ spotipy

# Comando para ejecutar tu aplicación 
CMD ["python3","-i", "index.py"]
