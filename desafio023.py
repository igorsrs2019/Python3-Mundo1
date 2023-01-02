#Este program recebe um numero de 4 digitos, e mostra na tela cada digito separado.
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o número {}'.format(num))
print ('Unidade {}'.format(u))
print ('Dezena {}'.format(d))
print ('Centena {}'.format(c))
print ('Milhar {}'.format(m))