# O Programa solicita 4 nomes e exibe um
from random import choice

n1 = input('Digite o primeiro nome: ')
n2 = input ('Digite o segundo nome: ')
n3 =  input ('Digite o terceiro nome: ')
n4 = input ('Digite o quarto nome: ')
escolhido = choice ( (n1, n2, n3, n4))
print ('Entre os 4 nomes digitados, o escolhido foi {}'.format(escolhido))