# Import required libraries
import streamlit as st
import yfinance as yf
import google.generativeai as genai
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go

# Configure Google Gemini
GOOGLE_API_KEY = "AIzaSyCuv5PR6TN475s9m5pKFNLBy_z0cMA0Nx4"  # Store this securely!
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_stock_data(symbol, period='1y'):
    """Get stock data using yfinance"""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        info = stock.info
        return {
            'history': hist,
            'info': info
        }
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {str(e)}")
        return None

def generate_stock_analysis(prompt, context):
    """Generate analysis using Gemini"""
    try:
        full_prompt = f"""As a stock market analyst, analyze the following information and answer the question.
        
        Context: {context}
        
        Question: {prompt}
        
        Please provide a clear and concise analysis based on the given data."""
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating analysis: {str(e)}"

def create_stock_chart(data, symbol):
    """Create a stock price chart using plotly"""
    fig = go.Figure(data=[
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close']
        )
    ])
    
    fig.update_layout(
        title=f"{symbol} Stock Price",
        yaxis_title="Price (USD)",
        xaxis_title="Date",
        template="plotly_white"
    )
    
    return fig

def main():
    st.set_page_config(page_title="Stock Analysis App", layout="wide")
    st.title("Stock Analysis with AI Assistant")
    
    # Sidebar for stock selection
    st.sidebar.title("Settings")
    symbol = st.sidebar.text_input("Enter Stock Symbol", value="AAPL").upper()
    period = st.sidebar.selectbox(
        "Select Time Period",
        ["1mo", "3mo", "6mo", "1y", "2y", "5y"],
        index=3
    )
    
    # Initialize session state for chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Fetch and display stock data
        data = get_stock_data(symbol, period)
        
        if data:
            # Display stock chart
            st.plotly_chart(create_stock_chart(data['history'], symbol))
            
            # Display key metrics
            metrics = st.columns(4)
            with metrics[0]:
                st.write("Current Price", f"${data['info'].get('currentPrice', 'N/A'):,.2f}")
            with metrics[1]:
                st.write("Market Cap", f"${data['info'].get('marketCap', 0):,.0f}")
            with metrics[2]:
                st.write("P/E Ratio", f"{data['info'].get('trailingPE', 'N/A'):,.2f}")
            with metrics[3]:
                st.write("52W High", f"${data['info'].get('fiftyTwoWeekHigh', 'N/A'):,.2f}")
    
    with col2:
        st.subheader("AI Assistant")
        st.info("Ask questions about the stock and get AI-powered analysis!")
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask about the stock..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Prepare context for AI
            context = f"""
            Stock Symbol: {symbol}
            Current Price: ${data['info'].get('currentPrice', 'N/A')}
            Market Cap: ${data['info'].get('marketCap', 'N/A'):,.2f}
            52 Week High: ${data['info'].get('fiftyTwoWeekHigh', 'N/A')}
            52 Week Low: ${data['info'].get('fiftyTwoWeekLow', 'N/A')}
            P/E Ratio: {data['info'].get('trailingPE', 'N/A')}
            Volume: {data['info'].get('volume', 'N/A')}
            Description: {data['info'].get('longBusinessSummary', 'N/A')}
            """
            
            # Generate response
            response = generate_stock_analysis(prompt, context)
            
            # Add AI response
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

if __name__ == "__main__":
    main()