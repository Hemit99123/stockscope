import yfinance as yf
import datetime as dt
import streamlit as st
start2 = dt.datetime(1700,1,1)
end2 = dt.datetime.now()
st.set_page_config(page_title='Stock App', page_icon='https://preview.pixlr.com/images/800wm/100/1/1001398554.jpg')

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
Dividends of
""" + ticker.upper())
tickerData.dividends
st.write("""
Other stocks you can buy other then 
""" + ticker.upper())
tickerData.recommendations

st.write("""
#### Author: Hemit Patel
#### Created: 2021-12-22 or December 12th 2021

"""
)
