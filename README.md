# Python_Pandas

Cenário: Todo mês é necessario cruzar 2 ou mais planilhas retiradas do sistema ERP para mapear a quantidade de estoque em DIAS

Trabalho moroso de limpar, juntar, apresentar os dados para diretoria.

![image](https://user-images.githubusercontent.com/64210900/156970757-eb0665e1-bb11-48fc-8395-e26cc0a07e36.png)


Com o pandas automatizamos o trabalho que antes levava horas para realizar.

Agora nosso processo dura apenas alguns minutos.


PASSO A PASSO >>>

1 - Extrair os Relatorios do ERP (218Bruto.csv e 221114Bruto.csv) separados por ; no diretorio do projeto

2 - Executar o TratarRelatorio218.py

3 - Executar o TratarRelatorio221114.py

* Após etapas 2 e 3 sera gerado os arquivos locais 218 e 221114 (Tratados) que serve apenas para a função abaixo coletar e juntar

4 - Executar o TratarRelatorio221114.py

* Após passo 4 sera gerado o resultado Final ResultadoGeral.html

![Resultado Final](https://user-images.githubusercontent.com/64210900/156970211-75bb0576-e2b1-4f17-a6f1-6f655fbb9400.PNG)


OBS: Ainda não tive tempo de implementar funções interligadas para automatizar o processo dentro do python, porem atualizarei o projeto conforme disponibilidade.
