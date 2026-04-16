# Crypto Tracker Real-Time (Proyecto DevOps)

## Descripción del Proyecto
Este proyecto es una aplicación web contenerizada que consulta y muestra el precio de criptomonedas. Fue desarrollada para implementar el ciclo de vida de operaciones DevOps, automatizando el despliegue mediante Bash y gestionando la infraestructura como código en AWS.

## Arquitectura y Tecnologías
El sistema funciona bajo una arquitectura de microservicios:
* **Frontend:** Servidor Nginx (HTML/JS/CSS).
* **Backend:** API REST con Flask (Python) implementando políticas CORS.
* **Base de Datos:** MongoDB.
* **Infraestructura:** Docker Compose, AWS EC2 (Amazon Linux 2023) y S3 (vía CloudFormation).

## Puertos Utilizados
* `80` - Frontend (Público)
* `8080` - Backend API (Público, para peticiones del cliente)
* `27017` - MongoDB (Interno, solo red de Docker)
* `22` - SSH (Para administración)

## Instrucciones de Ejecución Local
1. Clonar este repositorio.
2. Asegurar que Docker y Docker Compose estén instalados.
3. Ejecutar el script de despliegue: `./deploy.sh`
4. Acceder en el navegador a `http://localhost`

## Instrucciones de Despliegue en AWS EC2
1. Ejecutar el archivo `cloudformation/template.yaml` en la consola de AWS para provisionar la instancia y el bucket S3.
2. Conectarse a la instancia vía SSH.
3. Clonar el repositorio y ejecutar `./deploy.sh`.
4. El sistema incluye rutinas en `crontab` que automatizan el encendido/apagado usando los scripts `start_app.sh` y `stop_app.sh`.

