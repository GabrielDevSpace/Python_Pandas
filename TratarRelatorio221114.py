# Tutorial Retirado do site a seguir
# https://aprendizadodemaquina.com/artigos/customizando-suas-tabelas-no-pandas/
import pandas as pd

df = pd.read_csv('221114Bruto.csv', sep=';', engine='python', encoding='latin-1')

df.rename(
    columns={'departamento' : 'DEPARTAMENTO', 'Saldo Atual' : 'SALDO_ATUAL', 'Preco Custo' : 'TOTAL_CUSTO', 'Preço de Venda' : 'TOTAL_VALOR_ESTOQUE'},
    inplace=True
)

df["TOTAL_CUSTO"] = df["TOTAL_CUSTO"].astype(str)
df['TOTAL_CUSTO'] = df['TOTAL_CUSTO'].str.replace('[R$]', '', regex=True)
df['TOTAL_CUSTO'] = df['TOTAL_CUSTO'].str.replace(' ', '')
df['TOTAL_CUSTO'] = df['TOTAL_CUSTO'].str.replace('.', '', regex=True)
df['TOTAL_CUSTO'] = df['TOTAL_CUSTO'].str.replace(',', '.', regex=True)
df["TOTAL_CUSTO"] = df["TOTAL_CUSTO"].astype(float)

df["TOTAL_VALOR_ESTOQUE"] = df["TOTAL_VALOR_ESTOQUE"].astype(str)
df['TOTAL_VALOR_ESTOQUE'] = df['TOTAL_VALOR_ESTOQUE'].str.replace('[R$]', '', regex=True)
df['TOTAL_VALOR_ESTOQUE'] = df['TOTAL_VALOR_ESTOQUE'].str.replace(' ', '')
df['TOTAL_VALOR_ESTOQUE'] = df['TOTAL_VALOR_ESTOQUE'].str.replace('.', '', regex=True)
df['TOTAL_VALOR_ESTOQUE'] = df['TOTAL_VALOR_ESTOQUE'].str.replace(',', '.', regex=True)
df["TOTAL_VALOR_ESTOQUE"] = df["TOTAL_VALOR_ESTOQUE"].astype(float)

pivot = pd.pivot_table(df, index = ['DEPARTAMENTO'], values = ['SALDO_ATUAL','TOTAL_CUSTO','TOTAL_VALOR_ESTOQUE'], aggfunc = 'sum')
pivot.to_csv (r'221114Tratado.csv', encoding='utf-8')
