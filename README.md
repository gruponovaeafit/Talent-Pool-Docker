# Talent Pool Docker

### Instalación de Docker

Para instalar Docker en la instancia de Ubuntu, se deben seguir los siguientes pasos:

1. Instalar Docker:

   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo apt install git -y
   sudo systemctl enable docker
   sudo systemctl start docker
   ```

2. Agregar el usuario al grupo de Docker:

   ```bash
   sudo usermod -aG docker $USER
   ```

3. Cerrar la sesión y volver a iniciarla.

## Descargar la imagen de DockerHub

Para descargar la imagen de DockerHub, se deben ejecutar el siguiente comando:

```bash
docker pull msosav/talent-pool-docker:latest
```

## Ejecutar la imagen de DockerHub

Para ejecutar la imagen de DockerHub, se deben ejecutar el siguiente comando:

```bash
docker run -d -p 80:80 msosav/talent-pool-docker:latest
```

## Acceder a la aplicación

Para acceder a la aplicación, se debe abrir un navegador web y acceder a la dirección IP de la instancia por medio de HTTP.

## Comandos útiles de Docker

A continuación, se presentan algunos comandos útiles de Docker:

- Ver contenedores en ejecución:

  ```bash
  docker ps
  ```

- Ver todos los contenedores:

  ```bash
  docker ps -a
  ```

- Detener un contenedor:

  ```bash
  docker stop <CONTAINER_ID>
  ```

- Eliminar un contenedor:

  ```bash
  docker rm <CONTAINER_ID>
  ```

- Eliminar todos los contenedores:

  ```bash
  docker rm -vf $(docker ps -aq)
  ```

- Ver imágenes:

  ```bash
  docker images
  ```

- Eliminar una imagen:

  ```bash
  docker rmi <IMAGE_ID>
  ```

- Eliminar todas las imágenes:

  ```bash
  docker rmi -f $(docker images -aq)
  ```

- Ver logs de un contenedor:

  ```bash
  docker logs <CONTAINER_ID>
  ```

- Acceder a un contenedor:

  ```bash
  docker exec -it <CONTAINER_ID> /bin/bash
  ```
