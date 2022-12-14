#Este programa recebe o salario do usuario e exibe com 15% de aumento
salario = float(input('Digire o seu salario R$'))
aumentosalario =  salario + (salario * 15 /100)
print('O salario informado é R${}, apos o aumento de 15% ficara R${}'.format(salario, aumentosalario))