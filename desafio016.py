#Este programa solicita um numero real e exibe a sua porcao inteira
from math import trunc
n = float (input('Digite um numero: ' ))
print('O valor digitado foi {} e o inteiro é {} '.format(n, trunc(n)))
