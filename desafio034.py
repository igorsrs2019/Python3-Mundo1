#Este programa recebe o salário e adiciona um aumento de 10% se o salario for igual ou acima de R$ 1250,00, e se for abaixo recebe o aumento de 15%
s = float (input('Digite o seu salário R$: '))

if s >= 1250.00:
    print ('Seu salário é R${} seu aumento é de 10%, ao total vai ficar R${}'.format(s, ((s * 10) /100) + s))
else:
    print ('Seu salário é R${} seu aumento é de 15%, ao total vai ficar R${}'.format(s, ((s * 15) /100) + s ))