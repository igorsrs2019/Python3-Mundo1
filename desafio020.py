#Este programa recebe o nome dos alunos e exibe a ordem sorteada
from random import sample

n1 = (input('Digite o primeiro nome: '))
n2 = (input('Digite o segundo nome: '))
n3 = (input('Digite o terceiro nome: '))
n4 = (input('digite o quarto nome: '))
ordenacao = sample([n1, n2, n3, n4], k=4)
print("A ordem de apresentacao dos alunos é: {}".format(ordenacao))