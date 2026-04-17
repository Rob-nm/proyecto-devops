# 1. Usar una versión ligera de Python
FROM python:3.9-slim

# 2. Crear una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requisitos e instalar las librerías
COPY requirements.txt .
RUN pip install flask flask-cors pymongo

# 4. Copiar todo el código del backend a la carpeta /app
COPY . .

# 5. Abrir el puerto 8080 para que podamos entrar
EXPOSE 8080

# 6. Comando para arrancar la aplicación
CMD ["python", "app.py"]

