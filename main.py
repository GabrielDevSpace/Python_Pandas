# Tutorial Retirado do site a seguir
# https://aprendizadodemaquina.com/artigos/customizando-suas-tabelas-no-pandas/
import pandas as pd

df = pd.read_csv('sales_data_sample.csv', sep=',', engine='python', encoding='latin-1')

df.rename(
    columns={'YEAR_ID' : 'ANO', 'DEALSIZE' : 'TAMANHO', 'SALES': 'VENDAS'},
    inplace=True
)
df['TAMANHO'] = df['TAMANHO'].replace(
    {'Large': 'Grande', 'Medium': 'Médio', 'Small': 'Pequeno'}
)

# PIVOT

pivot = pd.pivot_table(df, index = ['ANO', 'TAMANHO'],
                       values = 'VENDAS', aggfunc = 'sum')

pivot.style.format({'VENDAS':'R$ {:,.0f}'})

pivot

# FUNÇÂO

def destaca_maiores_valores(valor):
   cor = 'blue' if valor > 1000000 else 'black'
   return f'color: {cor}'

pivot_highlight = pivot.style.format({'VENDAS':'R$ {:,.0f}'})\
   .highlight_max(color='green')\
   .highlight_min(color='red')

pivot_highlight


html = pivot.to_html()

#write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
