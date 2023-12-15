#pandas-> integrar python com excel
#twilio-> integrar python com sms
#openpyxl-> integrar python com o excel 
import pandas as pd

#passo a passo da solução:

#abrir os 6 arquivos em excel
lista_meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho']
tabela_vendas = pd.read_excel('janeiro.xlsx')
#para cada arquivo:
print(tabela_vendas)
#verificar s ealgum valor na coluna vendas daquele arquivo é maior que 55.000

#se for maior do que 55.000 -> envia um sms com o nome, o mês e as vendas do vendedor

#se não -> não fazer nada