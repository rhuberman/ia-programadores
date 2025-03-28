# Project README

## Libraries Used
- **FastAPI**: A modern web framework for building APIs with Python 3.6+.
- **sse_starlette**: For Server-Sent Events (SSE) to enable real-time updates.
- **OpenAI**: To interact with OpenAI's API for chat completions.
- **RedisVectorCache**: Caching mechanism using Redis for efficient data retrieval.
- **GoogleAPI**: For performing searches using Google’s API.
- **ScraperLocal**: Handles local web scraping tasks.
- **Playwright**: For browser automation to scrape web pages that require JavaScript execution.
- **aiohttp**: Asynchronous HTTP client for making requests.

## Environment Variables
1. Create a `.env` file in the project root directory.
2. Define the necessary environment variables as specified in the `.env.example` file.

## Building and Running the Application
1. Navigate to the project directory.
2. Run the following command to build the services:
   ```bash
   docker-compose up --build
   ```
3. Access the orchestrator API at `http://localhost:8000`.
4. Access the frontend at `http://localhost:8501`.

## Scraper Classes
- **ScraperLocal**: This class is used to scrape data from local sources.
- **ScraperRemote**: This class is used to scrape data from remote sources.

## Accessing the Chatbot
To interact with the chatbot, send a request to the `/streamingSearch` endpoint with your query.

## OpenAPI JSON Specification
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "API Documentation",
    "version": "1.0.0"
  },
  "paths": {
    "/streamingSearch": {
      "get": {
        "summary": "Streams search results",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "A stream of search results"
          }
        }
      }
    },
    "/scrape": {
      "post": {
        "summary": "Scrapes HTML content from a URL",
        "parameters": [
          {
            "name": "url",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "HTML content of the page",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "html": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "408": {
            "description": "Request timeout"
          }
        }
      }
    }
  }
}
