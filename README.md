# StockPulse

StockPulse is a real-time stock prediction and sentiment analysis platform that leverages current news data and advanced language models to forecast which stocks are likely to rise or fall. The project features a modern React frontend combined with backend services built using FastAPI, Flask, and Streamlit. It utilizes the News API for real-time news data fetching, NLTK’s VADER for robust sentiment analysis, and retrieval-augmented generation (RAG) on a large language model (LLM) to produce human-readable explanations behind predictions.

## Features

- **Real-Time Data Fetching:**  
  Retrieves up-to-date news articles using the News API to reflect current market conditions.

- **Advanced Sentiment Analysis:**  
  Uses NLTK’s VADER sentiment analyzer for accurate evaluation of news headlines rather than basic bag-of-words methods.

- **Stock Prediction & Explanation:**  
  Aggregates sentiment from news and alternative data (dummy for now) to predict whether a stock will be positively or negatively affected. An LLM is employed with RAG techniques to generate clear, natural language explanations for the predictions.

- **Multi-Backend Architecture:**  
  - **FastAPI:** Serves as the primary API server.
  - **Flask & Streamlit:** Power additional services and interactive dashboards.
  
- **Interactive Frontend:**  
  Built using **React** to provide a dynamic and responsive user interface.

## Architecture

- **Frontend:**  
  Developed in **React**, it communicates with our backend APIs to display analysis results and detailed explanations.

- **Backend:**  
  - **FastAPI:** Exposes RESTful endpoints to perform real-time sentiment analysis and prediction.
  - **Flask & Streamlit:** Support additional microservices and interactive visualizations.
  
- **Data Sources:**  
  - **News API:** Provides the latest news articles for sentiment analysis.
  
- **LLM & RAG:**  
  Utilizes an LLM (EleutherAI's GPT-Neo) combined with retrieval-augmented generation techniques to generate natural language explanations.

## Setup & Installation

### Prerequisites

- Python 3.8 or later
- Node.js and npm (for the React frontend)
- pip

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone repo link
   cd StockPulse

  # Algorithm Alchemists
  - Aman Singh
  - Deepansh Garg
  - Pulkit Pathak
  - Yatin Thakral
