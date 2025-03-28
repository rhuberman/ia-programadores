# Project README

## Introduction
Este proyecto es un chatbot conversacional de IA que utiliza varias tecnologías para realizar web scraping y procesamiento de lenguaje natural. El proyecto se encuentra en la carpeta `CAP03_CHALLENGE/project`.

## Libraries Used
- **aiohttp**: Utilizado por `ScraperLocal` para realizar web scraping de manera asíncrona.
- **Playwright**: Utilizado por `ScraperRemote` para renderizar JavaScript en un contenedor separado.
- **FastAPI**: Framework para construir la API del chatbot.
- **OpenAI**: Utilizado para generar embeddings y procesamiento de lenguaje natural.

## Environment Variables Configuration
Para configurar las variables de entorno, sigue estos pasos:

1. Crea un archivo `.env` en la raíz del proyecto.
2. Añade las siguientes variables de entorno al archivo `.env`:
    ```env
    OPENAI_API_KEY=tu_clave_api_de_openai
    SCRAPER_TYPE=ScraperLocal # o ScraperRemote
    ```

## Building and Running the Application
Sigue estos pasos para construir y ejecutar la aplicación:

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd CAP03_CHALLENGE/project
    ```

2. Construye y ejecuta los contenedores Docker:
    ```sh
    docker-compose up --build
    ```

3. La aplicación estará disponible en [http://localhost:8501/](http://localhost:8501/).

## Scraper Classes
El proyecto incluye dos clases de scraper:

- **ScraperLocal**: Utiliza `aiohttp` para el web scraping (por defecto).
- **ScraperRemote**: Utiliza `Playwright` en un contenedor replicado separado para un renderizado de JavaScript más complejo.

Para cambiar entre las clases de scraper, modifica el archivo `orchestrator/main.py` y descomenta los servicios scraper y lb-scraper apropiados en `docker-compose.yml`.

## Accessing the Chatbot
Después de ejecutar la aplicación, abre tu navegador web y navega a [http://localhost:8501/](http://localhost:8501/) para interactuar con el chatbot.

## OpenAPI Definition
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/streamingSearch": {
      "get": {
        "summary": "Realiza una búsqueda en streaming",
        "responses": {
          "200": {
            "description": "Resultado de la búsqueda"
          }
        }
      }
    }
  }
}