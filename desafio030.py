# Este programa le um numero e informa se é impar ou par

n = int(input('Digite um numero: '))
d = n % 2
if d == 0:
    print('O numero digitado foi {} este numero é par'.format(n))
else:
    print('O numero digitado foi {} este numero é impar'.format(n))    