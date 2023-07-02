#CÓDIGO DE VISUALIZAÇÃO DE DADOS
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_pd = pd.read_csv('gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
  gasolina_grafico= sns.lineplot(data=gasolina_pd, x='dia', y='venda')
  gasolina_grafico.set(title='Preço da gasolina - São Paulo - Julho de 2021', xlabel='Dia', ylabel='Preço médio (R$)')
  plt.savefig('gasolina.png')