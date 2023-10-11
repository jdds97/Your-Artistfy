FROM python:3.12.0-slim-bullseye
WORKDIR /app/src
COPY . /app/src/
RUN  pip install -r requirements.txt
ENTRYPOINT python3 index.py
pyt