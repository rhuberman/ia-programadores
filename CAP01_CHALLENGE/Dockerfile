# Usa una imagen base oficial de Python
FROM python:3.9-slim
##FROM python:3.12-venv
# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación en el contenedor
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]