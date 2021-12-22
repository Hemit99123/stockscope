import yfinance as yf
import datetime as dt
import streamlit as st
start = dt.datetime(1700,1,1)
end = dt.datetime.now()
st.set_page_config(page_title='Stock App')

st.write(""" 
# STOCK APP

#### Instructions:

Delete the placeholder "GOOGL" and then search the ticker that you wish.
If you wish to compare stocks just input both of your tickers e.g. AAPL GOOGL

This will compare stocks in APPLE and GOOGLE!
""")
ticker = st.text_input('TICKER')

if ticker !== None:
   Stock = yf.download(ticker, start, end)
  st.write(""" 
  Closing price of 
  """ + ticker)
  st.line_chart(Stock.Close)
  st.write(""" 
  Volume price of
  """ + ticker)
  st.line_chart(Stock.Volume)
else:
    st.write("""
  Please enter an input.
  """) 

st.write("""
#### Author: Hemit Patel
#### Created: 2021-12-22 or December 12th 2021

"""
)
