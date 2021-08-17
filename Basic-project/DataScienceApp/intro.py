import yfinance as yf
import streamlit as st

st.write("""
    # Simple stock price app
    Shown are the stock closing price and volume of Google
""")

googl = 'GOOGL'
tickedData = yf.Ticker(googl)
tickerDf = tickedData.history(
    period='id', start='2010-08-15', end='2021-08-15')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
