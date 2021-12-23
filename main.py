import yfinance as yf
import datetime as dt
import streamlit as st
start2 = dt.datetime(1700,1,1)
end2 = dt.datetime.now()
st.set_page_config(page_title='Stock App')

st.write(""" 
# STOCK APP

#### Instructions:

Delete the placeholder "GOOGL" and then search the ticker that you wish.
If you wish to compare stocks just input both of your tickers e.g. AAPL GOOGL

This will compare stocks in APPLE and GOOGLE!
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
Institutional of 
""" + ticker.upper())
tickerData.institutional_holder
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
