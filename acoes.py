import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta

# Título da aplicação
st.title('Monitor de Ações Financeiras - Múltiplas Ações')

# Definindo uma lista de ações exemplo
acoes_disponiveis = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BEEF3.SA', 'PETR4.SA', 'VALE3.SA']

# Seleção múltipla de ações
acoes_selecionadas = st.multiselect('Selecione as ações que deseja visualizar:', acoes_disponiveis, default=['AAPL', 'MSFT', 'GOOGL', 'AMZN'])

# Selecionando o intervalo
interval_options = {
    'Daily': '1d',
    'Weekly': '1wk',
    'Monthly': '1mo'
}
interval_choice = st.selectbox('Escolha o intervalo:', list(interval_options.keys()))

# Obtendo a data inicial e final
dt_start = datetime.today() - timedelta(days=30)
dt_end = datetime.today()

# Loop através das ações selecionadas e mostrar os dados de cada uma
for ticker in acoes_selecionadas:
    st.write(f'### Dados da ação: {ticker}')
    try:
        # Obtendo os dados da ação usando yfinance
        ticker_data = yf.Ticker(ticker)
        df = ticker_data.history(start=dt_start.strftime('%Y-%m-%d'), end=dt_end.strftime('%Y-%m-%d'), interval=interval_options[interval_choice])

        # Verifica se há dados disponíveis
        if not df.empty:
            # Exibindo os dados
            st.dataframe(df)

            # Exibindo o gráfico de preços de fechamento
            st.line_chart(df['Close'], width=700, height=400)
        else:
            st.write(f"Não há dados disponíveis para o período selecionado da ação {ticker}.")

    except Exception as e:
        st.write(f"Ocorreu um erro ao carregar os dados da ação {ticker}: {e}")
