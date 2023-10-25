# Docker - Practica <!-- omit in toc -->

- [Prerequisitos](#prerequisitos)
- [Dockerhub](#dockerhub)
- [Corramos nuestros propios ejemplos](#corramos-nuestros-propios-ejemplos)
  - [00.Comandos](#00comandos)
  - [01.hello-world](#01hello-world)
  - [02.nyancat](#02nyancat)
  - [02.snake](#02snake)
  - [03.web](#03web)
  - [04.resumir](#04resumir)
- [Ideas](#ideas)

## Prerequisitos

Instalar Docker Desktop.

- Si no lo hiciste ya, [instalalo](https://docs.docker.com/desktop/install/windows-install/).
- Si se complica, acá hay un [video](https://www.youtube.com/watch?v=ZO4KWQfUBBc&ab_channel=FaztCode) de como instalarlo.
- Si se complica más, avisen :grin:

## Dockerhub

Nosotros podemos crear nuestras imagenes con el dockerfile. Pero tenemos también repositorios, lugares donde está lleno de imagenes/plantillas que otros crearon -> [Dockerhub](https://hub.docker.com/).

Ejemplos famosos:

- [Hello-world](https://hub.docker.com/_/hello-world)
- [Windows](https://hub.docker.com/_/microsoft-windows)
- [Ubuntu](https://hub.docker.com/_/ubuntu)
- [Python](https://hub.docker.com/_/python/tags)

## Corramos nuestros propios ejemplos

Primero provemos que funciona:

```bash
$ docker -v

Docker version 20.10.22, build 3a2c30b
```

### 00.Comandos

```bash
# Help
$ docker --help
# Ver Imagenes
$ docker image ls
# Ver containers
$ docker container ls
```

### 01.hello-world

[Referencia](https://hub.docker.com/_/hello-world)

```bash
$ docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
70f5ac315c5a: Pull complete 
Digest: sha256:88ec0acaa3ec199d3b7eaf73588f4518c25f9d34f58ce9a0df68429c5af48e8d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### 02.nyancat

Este container es algo inútil pero divertido :rolf: Basado en este [repo](https://hub.docker.com/r/wernight/funbox).

```sh
$ docker run --rm -it wernight/funbox nyancat 
```

En [dockerhub](https://hub.docker.com/r/wernight/funbox).

### 02.snake 

Desde este [repo](https://github.com/DyegoCosta/snake-game).

```sh
$ docker run -ti dyego/snake-game
```
Una aplicación muy simple, pero que nos sirve para ver como se puede correr una aplicación en docker. En este caso un snake game.

### 03.web

Docker compose. Hay una otra forma de correr contenedores = docker compose. Esto nos permite correr varios contenedores a la vez. En este caso vamos a correr una aplicación web con angular.

```bash
cd 03.web/angular
docker compose up
```

Este contenedor va a correr en la computadora local en el puerto 4200. Para acceder a la aplicación web, vamos a tener que ir a [localhost:4200](http://localhost:4200/).

Si lo paramos con `ctrl + c`, vamos a ver que el contenedor se detiene. Y si vamos a localhost:4200, no vamos a poder acceder a la aplicación web.

Si lo corremos con `docker compose up -d`, el contenedor se va a correr en segundo plano.

### 04.resumir

```bash
cd 04.resumir
docker build . -t resumir:latest
docker run --name resumir -it resumir:latest
docker run --rm -v data:/app/data -w /app  --name resumir -i -t resumir:latest
```

Revisenmos la última: `docker run --rm -v data:/app/data -w /app  --name resumir -i -t resumir:latest`

- --rm -> remove
- -v -> volume
- -w -> working directory
- --name -> nombre

## Ideas

- Kahoot?
- Review de 1 o 2 ideas generales (PPT)
- Instalar docker desktop
  - Quien no lo tiene instalado le va a tocar instalar
- Docker -v
- Docker help
- Docker run hello-world
- Docker web - Angular
- Docker flask
- Docker summary
