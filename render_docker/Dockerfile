# Utilizamos una imagen base de Python
ARG PYTHON_VERSION=3.12.8	
FROM python:${PYTHON_VERSION} as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el requirements.txt y lo instalamos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiamos el resto de los archivos de la aplicación
COPY . .

# Exponemos el puerto (ajusta según tu aplicación)
EXPOSE 8000

# Comando para iniciar la aplicación (ajusta según tu aplicación)
CMD uvicorn main:app --reload --port 8000 --host 0.0.0.0
