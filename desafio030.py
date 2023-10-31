# Este programa le um numero e informa se é impar ou par

numero = int(input('Digite um numero: '))
resultado = numero % 2
if resultado == 0:
    print('O numero digitado foi {} este numero é PAR'.format(numero))
else:
    print('O numero digitado foi {} este numero é IMPAR'.format(numero))    