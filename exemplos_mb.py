# Tutorial Retirado do site a seguir
# https://aprendizadodemaquina.com/artigos/customizando-suas-tabelas-no-pandas/
import pandas as pd

df = pd.read_csv('exemplos_mb.csv', sep=';', engine='python', encoding='latin-1')

df.rename(
    columns={'departamento' : 'DEPARTAMENTO', 'Custo de Compra Médio Faturado (+) Impostos (CMV)' : 'CUSTO', 'R$ Valor de Venda Faturado com S.T. e DF' : 'FATURAMENTO'},
    inplace=True
)

# Pivot
df['CUSTO'] = df['CUSTO'].astype(str)
df['CUSTO'] = df['CUSTO'].str.replace('R$', '.')


pivot = pd.pivot_table(df, index = ['DEPARTAMENTO'], values = ['FATURAMENTO','CUSTO'], aggfunc = 'sum')

html = df.to_html()

#write html to file
text_file = open("exemplo_mb.html", "w")
text_file.write(html)
text_file.close()
