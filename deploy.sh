#!/bin/bash

echo "🚀 Iniciando despliegue del proyecto..."

# 1. Actualizar desde GitHub (esto lo usaremos después)
# git pull origin main

# 2. Construir y levantar los contenedores
echo "📦 Construyendo contenedores..."
sudo /usr/local/bin/docker-compose up --build -d

echo "✅ Despliegue completado. La app está corriendo en el puerto 80."
