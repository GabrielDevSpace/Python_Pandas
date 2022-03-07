# Tutorial Retirado do site a seguir
# https://aprendizadodemaquina.com/artigos/customizando-suas-tabelas-no-pandas/
import pandas as pd

df = pd.read_csv('218Bruto.csv', sep=';', engine='python', encoding='latin-1')

df.rename(
    columns={'Quantidade Vendida' : 'QTD_VENDIDA','departamento' : 'DEPARTAMENTO', 'Custo de Compra Médio Faturado (+) Impostos (CMV)' : 'CUSTO', 'R$ Valor de Venda Faturado com S.T. e DF' : 'FATURAMENTO'},
    inplace=True
)

# Pivot
df["FATURAMENTO"] = df["FATURAMENTO"].astype(str)
df['FATURAMENTO'] = df['FATURAMENTO'].str.replace('[R$]', '', regex=True)
df['FATURAMENTO'] = df['FATURAMENTO'].str.replace(' ', '')
df['FATURAMENTO'] = df['FATURAMENTO'].str.replace('.', '', regex=True)
df['FATURAMENTO'] = df['FATURAMENTO'].str.replace(',', '.', regex=True)
df["FATURAMENTO"] = df["FATURAMENTO"].astype(float)

df["CUSTO"] = df["CUSTO"].astype(str)
df['CUSTO'] = df['CUSTO'].str.replace('[R$]', '', regex=True)
df['CUSTO'] = df['CUSTO'].str.replace(' ', '')
df['CUSTO'] = df['CUSTO'].str.replace('.', '', regex=True)
df['CUSTO'] = df['CUSTO'].str.replace(',', '.', regex=True)
df["CUSTO"] = df["CUSTO"].astype(float)

df["QTD_VENDIDA"] = df["QTD_VENDIDA"].astype(str)
df['QTD_VENDIDA'] = df['QTD_VENDIDA'].str.replace('[R$]', '', regex=True)
df['QTD_VENDIDA'] = df['QTD_VENDIDA'].str.replace(' ', '')
df['QTD_VENDIDA'] = df['QTD_VENDIDA'].str.replace('.', '', regex=True)
df['QTD_VENDIDA'] = df['QTD_VENDIDA'].str.replace(',', '.', regex=True)
df["QTD_VENDIDA"] = df["QTD_VENDIDA"].astype(float)

pivot = pd.pivot_table(df, index = ['DEPARTAMENTO'], values = ['FATURAMENTO','CUSTO','QTD_VENDIDA'], aggfunc = 'sum')
pivot.to_csv (r'218Tratado.csv', encoding='utf-8')
