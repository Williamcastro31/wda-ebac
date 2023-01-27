# código de geração do gráfico 

# baixando pacotes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ler arquivo CSV
df_gasolina = pd.read_csv('gasolina.csv')

# geração do gráfico

grafico_gasolina = sns.lineplot(data=df_gasolina, x='dia', y='venda', palette='BuGn')
grafico_gasolina.set(title='Hitórico de Preço da Gasolina (JULHO/2021)', xlabel='Dia', ylabel='Venda');

# salvando imagem
plt.savefig('/content/wda-ebac/gasolina.png')
