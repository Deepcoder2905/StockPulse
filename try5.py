import streamlit as st
import google.generativeai as genai
import requests
import json
import time


# ============= CONFIGURATION =============
NEWS_API_KEY = "YOUR_API_KEY"  # Replace with your NewsAPI key
GEMINI_API_KEY = "YOUR_API_KEY"  # Replace with your Google AI key
genai.configure(api_key=GEMINI_API_KEY)

# ============= FETCH NEWS FROM NEWSAPI =============
@st.cache_data
def fetch_stock_news():
    url = f"https://newsapi.org/v2/everything?q=stocks&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [{"title": article["title"], "description": article["description"]} for article in articles]
    else:
        st.error("Error fetching news: " + str(response.json()))
        return []

# ============= EXTRACT COMPANY NAMES FROM NEWS =============
def extract_companies(news_article):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Extract company names from the following stock market-related news article:
    
    "{news_article}"
    
    Provide only company names in a comma-separated format.
    """
    response = model.generate_content(prompt)
    return response.text.split(", ") if response else []

# ============= HELPER: RETRY LOGIC FOR GEMINI API =============
def generate_content_with_retry(model, prompt, max_retries=5, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response
        except Exception as e:
            if "ResourceExhausted" in str(e) or "429" in str(e):
                wait_time = backoff_factor ** attempt
                st.write(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e
    raise Exception("Max retries exceeded.")

def extract_json_from_text(text):
    # Locate the first '{' and the last '}' to extract JSON
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        return text[start:end+1].strip()
    return text.strip()

# ============= FIND STOCK SYMBOLS FROM COMPANY NAMES USING GEMINI =============
def get_stock_symbols(company_names):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    For the following companies: {", ".join(company_names)},
    output ONLY a valid JSON object (with no markdown formatting or additional text)
    that maps each company name to its stock ticker symbol.
    - If an input is already a ticker symbol (e.g. "MSFT"), simply return that ticker symbol.
    - If a company does not have a publicly traded ticker, use "Unknown" as its value.
    
    For example, for inputs ["Apple", "MSFT"], a valid output is:
    {{
      "Apple": "AAPL",
      "MSFT": "MSFT"
    }}
    """
    try:
        response = generate_content_with_retry(model, prompt)
        raw_text = response.text
        json_text = extract_json_from_text(raw_text)
        stock_symbols = json.loads(json_text)
    except Exception as e:
        st.error("Error parsing JSON from Gemini: " + str(e))
        stock_symbols = {company: "Unknown" for company in company_names}
    
    # Replace "Unknown" symbols with the first word of the company name in uppercase
    for company, symbol in stock_symbols.items():
        if symbol.strip().lower() == "unknown":
            # Use the first word of the company name, capitalized
            stock_symbols[company] = company.split()[0].upper()
    return stock_symbols

# ============= ANALYZE MARKET IMPACT =============
def gemini_market_impact(news_article, company_names):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Given the news article:
    "{news_article}"
    
    Analyze how it might affect the following companies: {", ".join(company_names)}
    
    Provide a market impact assessment as:
    - Company Name: Sentiment (Positive, Negative, Neutral)
    - Market Impact: (High, Medium, Low)
    - Key takeaways for investors
    """
    response = model.generate_content(prompt)
    return response.text if response else "Analysis unavailable."

# ============= STREAMLIT APP MAIN FUNCTION =============
def main():
    st.title("Stock News Analysis")
    st.write("Fetch the latest stock market news, extract company names, get their stock symbols using Gemini, and analyze market impact.")
    
    if st.button("Fetch Latest Stock News"):
        st.info("Fetching latest stock news...")
        news_articles = fetch_stock_news()
        
        if not news_articles:
            st.error("No news articles found.")
            return
        
        for news in news_articles[:5]:  # Process top 5 news articles
            news_text = f"{news['title']} - {news['description']}"
            with st.expander(news['title']):
                st.write("**News:**")
                st.write(news_text)
                
                # Step 1: Extract Company Names
                companies = extract_companies(news_text)
                st.write("**Companies Mentioned:**", companies)
                
                if not companies:
                    st.warning("No relevant companies identified.")
                    continue
                
                # Step 2: Find Stock Symbols using Gemini in one response
                stock_symbols = get_stock_symbols(companies)
                st.write("**Stock Symbols:**", stock_symbols)
                
                # Step 3: Analyze Market Impact
                analysis = gemini_market_impact(news_text, companies)
                st.write("**Analysis:**", analysis)

if __name__ == "__main__":
    main()
