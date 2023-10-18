#Programa de Financiamento

valor_casa = float (input ('Valor da casa: R$'))
salario_comprador = float (input('Salario do comprador: R$'))
anos_financiamento = int (input('Quantos anos de financiamento? '))
valor_prestacao = valor_casa /(anos_financiamento * 12)

if (valor_prestacao > salario_comprador *  30 /100):
    print  ('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos_financiamento), end='')
    print (' a prestação será de R$ {:.2f}'.format(valor_prestacao))
    print ('Empréstimo NEGADO!')
else: 
    print ('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos_financiamento), end='')
    print (' a prestação será de R$ {:.2f}'.format(valor_prestacao))    
    print('Empréstimo CONCEDIDO!')
    
    




    
    



    




