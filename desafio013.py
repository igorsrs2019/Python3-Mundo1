#Este programa recebe o salario do usuario e exibe com 15% de aumento
salario = float(input('Qual é o salario do Funcionário R$ '))
novo =  salario + (salario * 15 /100)
print('O salario informado é R$ {:.2f}, com 15% de aumento passa a receber R$ {:.2f}'.format(salario, novo))