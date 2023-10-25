# Preguntas a un PDF <!-- omit in toc -->

Ref: <https://www.shakudo.io/blog/build-pdf-bot-open-source-llms>

- [Que hay en el repositorio](#que-hay-en-el-repositorio)
- [Dockerfile](#dockerfile)
- [Como ejecuto](#como-ejecuto)
- [Troubleshooting](#troubleshooting)

## Que hay en el repositorio

- ./Data: directorio con el pdf que lee, las preguntas y las respuestas
- Dockerfile: para crear la imagen de docker
- requirements.txt: para instalar las dependencias

## Dockerfile

```dockerfile
FROM python:3.9.18

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Run a command
CMD ["python", "main.py"]
```

Observaciones:

- FROM python:3.9.18:
  - imagen base
  - Python -> Lenguaje de programación que voy a usar

## Como ejecuto

- Build:
  - `docker build . -t llm_test:latest`
  - -t -> tag/alias
- Run:
  - `docker run --name resumir -it llm_test:latest`
- Run con un volumen: 
  - `docker  run  -v ./data:/app/data -w /app -i -t llm_test:latest --name resumir`
  - -v -> volume
  - -w -> working directory
  - -i -> interactive
  - -t -> tty/nombre
- Prender un contenedor que ya existe:
  - `docker start resumir `
- Apagar un contenedor que ya existe:
  - `docker stop resumir `
- Eliminar un contenedor que ya existe:
  - `docker rm resumir`

## Troubleshooting

En mi máquina local tuve que hacer esto:

```sh
pip install numpy scipy
pip install torch==2.1.0
pip install -r requirements.txt
```
