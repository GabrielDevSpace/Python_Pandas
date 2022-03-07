import pandas as pd

# Carregando minhas duas CSVs geradas anteriormente pelas funções 218Bruto.py e 221114Bruto.py
df_218 = pd.read_csv('218Tratado.csv', sep=',', engine='python', encoding='latin-1')
df_221114 = pd.read_csv('221114Tratado.csv', sep=',', engine='python', encoding='latin-1')

""" Merge é como o famoso PROCV do excell
Se existir uma primeira coluna com mesmo identificador em ambas planilhas o pandas ira realizar o merge
Em nosso Ex o identificador é DEPARTAMENTO
"""
resultado = pd.merge(df_221114, df_218)

""" Calculo Dias de Estoque
Para calcular quantos dias temos em estoque de tal produto utilizamos o calculo a seguir
ESTOQUE_ATUAL / ( QTDE_VENDIDA / periodo_analisado ) 
* Caso seus CSVs sejam de periodo de 30 60 90 ... é só modificar a var qtde_dias_analisado para o periodo de dias desejado
"""
periodo_analisado = 28  # Dias 01/02/2022 a 28/02/2022
resultado['.DIAS_ESTOQUE'] = round(resultado['SALDO_ATUAL'] / (resultado['QTD_VENDIDA'] / periodo_analisado),0)

# Abaixo temos um PIVOT = TABELA DINAMICA
pivot = pd.pivot_table(resultado, index = ['DEPARTAMENTO'], values = ['.DIAS_ESTOQUE','SALDO_ATUAL','TOTAL_CUSTO','TOTAL_VALOR_ESTOQUE','CUSTO','FATURAMENTO','QTD_VENDIDA'], aggfunc = 'sum')

# Sera criado um arquivo .html na raiz do projeto com o resultado.
html = pivot.to_html()
text_file = open("ResultadoGeral.html", "w")
text_file.write(html)
text_file.close()

# Temos tambem a opção de gerar outro CSV com o resultado
# pivot.to_csv (r'ResultadoGeral.csv', encoding='utf-8')