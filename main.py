import yfinance as yf
import datetime as dt
import streamlit as st
start = dt.datetime(1700,1,1)
end = dt.datetime.now()
st.write(""" 
# STOCK APP

#### Instructions:

Delete the placeholder "GOOGL" and then search the ticker that you wish.
""")
ticker = st.text_input('TICKER', value="GOOGL")

if ticker == '': 
  st.write("""
  # error null
  """) 
else:
  Stock = yf.download(ticker, start, end)
  st.write(""" 
  Closing price of 
  """ + ticker)
  st.line_chart(Stock.Close)
  st.write(""" 
  Volume price of
  """ + ticker)
  st.line_chart(Stock.Volume)
