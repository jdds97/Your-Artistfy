#!/bin/sh

# Crea un entorno virtual si no existe
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activa el entorno virtual
. venv/bin/activate


# Inicia tu aplicación (por ejemplo, el servidor Flask)
#python3 index.py
