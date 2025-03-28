# Web Scraper and ChatBot Project

This project consists of a web scraper that extracts information from websites and a chatbot that uses OpenAI's API to provide responses based on the scraped data.

## Table of Contents
- [Libraries and Dependencies](#libraries-and-dependencies)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Building and Running the Application](#building-and-running-the-application)
- [Scraper Classes](#scraper-classes)
- [Accessing the ChatBot](#accessing-the-chatbot)
- [OpenAI API Configuration](#openai-api-configuration)

## Libraries and Dependencies

The project uses the following libraries:

### Backend Dependencies
- **Express**: Web framework for Node.js to create HTTP server and API endpoints
- **Axios**: HTTP client for making requests to websites and APIs
- **Cheerio**: Library for parsing and manipulating HTML, used for web scraping
- **Dotenv**: Loads environment variables from a .env file
- **OpenAI**: Official OpenAI API client for Node.js
- **Cors**: Middleware to enable Cross-Origin Resource Sharing
- **Body-parser**: Middleware to parse incoming request bodies

### Frontend Dependencies
- **React**: JavaScript library for building user interfaces
- **React DOM**: React package for DOM rendering
- **Axios**: HTTP client for making requests to the backend API
- **React Router DOM**: Routing library for React applications

## Environment Variables

Create a `.env` file in the root directory with the following variables:

PORT=3001 
OPENAI_API_KEY=your_openai_api_key

Replace `your_openai_api_key` with your actual OpenAI API key.

## Project Structure

The project is organized into two main parts:
- Backend: Node.js server with Express
- Frontend: React application

## Building and Running the Application

### Backend Setup

1. Navigate to the project directory:

```bash
cd CAP03_CHALLENGE/project
```
2. Install dependencies:
npm install

3. Start the backend server:
npm run start:backend

The server will start on the port specified in your .env file (default: 3001).

## Frontend Setup
1. In a new terminal, navigate to the project directory:
cd CAP03_CHALLENGE/project

2. Start the frontend development server:
npm run start:frontend

The React application will start on port 3000 and can be accessed at http://localhost:3000.

## Scraper Classes
The project contains several scraper classes that extract information from different websites:

### BaseScraper
The base class that provides common functionality for all scrapers:

class BaseScraper {
  constructor() {
    this.axios = axios;
    this.cheerio = cheerio;
  }

  async fetchHTML(url) {
    try {
      const response = await this.axios.get(url);
      return response.data;
    } catch (error) {
      console.error(`Error fetching ${url}:`, error);
      return null;
    }
  }

  parseHTML(html) {
    return this.cheerio.load(html);
  }
}

### Specialized Scrapers
Each specialized scraper extends the BaseScraper and implements specific scraping logic for different websites:

NewsScraper: Extracts news articles from news websites
ProductScraper: Extracts product information from e-commerce websites
WeatherScraper: Extracts weather information from weather forecast websites
Each scraper implements methods to:

Connect to specific URLs
Extract relevant data using CSS selectors
Format and return the scraped data
Accessing the ChatBot
The chatbot can be accessed through the frontend interface or directly via API endpoints.

### Frontend Interface
1. Open your browser and navigate to http://localhost:3000
2. Use the chat interface to interact with the chatbot
3. Type your questions related to the scraped data

### API Endpoints
The chatbot can also be accessed directly through API endpoints:

POST /api/chat
Request body: { "message": "Your question here" }
Response: { "response": "Chatbot response" }
Example using curl:
curl -X POST http://localhost:3001/api/chat -H "Content-Type: application/json" -d '{"message":"Tell me about today's news"}'

## OpenAI API Configuration
The project uses OpenAI's API to power the chatbot. The configuration is as follows:
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant that provides information based on scraped web data. You can answer questions about news, products, and weather information that has been collected by our web scrapers."
    },
    {
      "role": "user",
      "content": "User's message here"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 500,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
}

This configuration:

Uses the GPT-3.5 Turbo model
Sets up the chatbot as a helpful assistant with context about the scraped data
Uses a temperature of 0.7 for a balance between creativity and accuracy
Limits responses to 500 tokens
Applies no frequency or presence penalties
The OpenAI API is called from the backend to ensure the API key remains secure and is not exposed to the client-side code.

This README provides a comprehensive guide to understanding, setting up, and using the web scraper and chatbot project. For more detailed information about specific components, refer to the code documentation within each file. EOL