from time import sleep
from datetime import date

print ('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: ')
ano = int (input('Digite um ano: '))
print ('ANALISANDO....')
sleep (2)
if ano == 0:
     ano = date.today().year
if     ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print ('Ano é bissexto: {} '.format(ano)) 
else:
      print ('Ano não é bissexto: {} '.format(ano))