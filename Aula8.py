#Streamlit: Case Bolsa de Valores

#Oq e o Yfinance

#Como usar?

import yfinance as yf
import pandas as pd
import streamlit as st

st.markdown('# Analisando empresas')

st.text_input('Ticker code', key='tickercode',value='GOOG')
st.markdown('## Noticias:')

ticken = st.session_state.tickercode
data = yf.Ticker(ticken)

data_news = pd.DataFrame(data.news)
st.dataframe(data_news)
#print(f'\n{data_news}')


data_hist = data.history(period ='max', start='2019-03-16',end='2023-03-16',interval='5d')
data_hist = data_hist.reset_index()

st.line_chart(data_hist, x = 'Date', y = 'Close')
#print(data_hist)