import yfinance as yf
import datetime as dt
import streamlit as st
start2 = dt.datetime(1700,1,1)
end2 = dt.datetime.now()
url = 'https://cdn-icons-png.flaticon.com/512/1369/1369860.png'
st.set_page_config(page_title='Stock App', page_icon=url)

st.write(""" 
# STOCK APP

#### Instructions:
Just type the ticker of your stock!
""")
ticker = st.text_input('TICKER')


tickerSymbol = ticker
tickerSymbol = ticker.strip()
tickerData = yf.Ticker(tickerSymbol)
Stock = tickerData.history(period='1d', start=start2, end=end2)
st.write(""" 
Closing price of 
""" + ticker.upper())
st.line_chart(Stock.Close)
st.write(""" 
Volume price of
""" + ticker.upper())
st.line_chart(Stock.Volume)
st.write(""" 
Institutional holders of 
""" + ticker.upper())
tickerData.institutional_holders
st.write("""
Other stocks you can buy other then 
""" + ticker.upper())
tickerData.recommendations

st.write("""
#### Author: Hemit Patel
#### Created: 2021-12-22 or December 12th 2021
"""
)
