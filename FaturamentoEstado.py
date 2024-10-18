import plotly.express as px
import pandas as pd

# Definindo o faturamento mensal por estado
dados = {
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'Faturamento': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

# Cria um DataFrame
df = pd.DataFrame(dados)

# Calcula o total de faturamento
total_faturamento = df['Faturamento'].sum()

# Calcula o percentual de cada estado
df['Percentual'] = (df['Faturamento'] / total_faturamento) * 100

# Cria o gráfico
fig = px.pie(df, 
             values='Percentual', 
             names='Estado', 
             title='Percentual de Faturamento por Estado',
             color='Estado'
             )  

# Exibindo o gráfico
fig.show()