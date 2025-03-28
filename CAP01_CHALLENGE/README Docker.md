# ia-programadores
IA para programadores
## Build
sudo docker build -t cap01_challenge .

## Ejecuta el contenedor
sudo docker run -d -p 8000:8000 cap01_challenge

## Lista los contenedores en ejecución:
sudo docker ps
## Lista todos los contenedores (incluidos los detenidos):
sudo docker ps -a
## Detén un contenedor en ejecución (si es necesario):
sudo docker stop <container_id>
## Elimina un contenedor específico:
sudo docker rm <container_id>
## Elimina todos los contenedores detenidos:
sudo docker container prune
