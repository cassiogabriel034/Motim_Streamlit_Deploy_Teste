import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime

st.markdown('# Analisando empresas')

st.text_input('Ticker code', key='tickercode',value='NFLX')

st.markdown(f'## Ultimas da Notícias da {st.session_state.tickercode}:')
ticker = st.session_state.tickercode

data = yf.Ticker(ticker)

data_news = pd.DataFrame(data.news)
# Expande a coluna 'content' que é um dicionário
content_expanded = data_news['content'].apply(pd.Series)
data_news2 = content_expanded[['title', 'contentType', 'canonicalUrl', 'displayTime']]

st.dataframe(data_news2)
#print(f'\nAAAAS: \n{content_expanded}')

end_data = datetime.now().strftime('%Y-%m-%d')
data_hist = data.history(period='max', start='2019-03-16', end=end_data, interval='5d')
data_hist = data_hist.reset_index()

st.markdown('# Construa seu grafico')

#index=list(data_hist.columns).index('Date')
ex = st.selectbox('Eixo x:', data_hist.columns, index=0)
#list(data_hist.columns).index('Close')
ey = st.selectbox('Eixo y:', data_hist.columns, index=4)

st.markdown(f'## Grafico {ey} X {ex}')
st.line_chart(data_hist, x = ex, y= ey)