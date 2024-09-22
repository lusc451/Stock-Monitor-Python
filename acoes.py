import yfinance as yf
import pandas as pd
import streamlit as st

#Definindo o ticker da ação
ticker_symbol = 'BEEF3.SA'

#Baixando dados históricos
ticker_data = yf.Ticker(ticker_symbol)
df = ticker_data.history(period='1mo', interval='1d')

#Exibindo os dados
# print(df)

# Configurando o Streamlit
st.title('Monitor de Ações Financeiras')

# Campo de entrada para o usuário selecionar a ação
stock_ticker = st.text_input('Digite o código da ação:', 'BEEF3.SA')

# Selecionando o intervalo
interval = st.selectbox('Escolha o intervalo:', ['1d', '5d', '1wk', '1mo', '3mo'])

# Carregando os dados da ação usando yfinance
ticker_data = yf.Ticker(stock_ticker)
df = ticker_data.history(period='1mo', interval=interval)

# Exibindo os dados
st.write(f'Dados da ação: {stock_ticker}')
st.dataframe(df)

# Exibindo o gráfico
st.line_chart(df['Close'])