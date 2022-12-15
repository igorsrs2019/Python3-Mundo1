#Este programa solicita a temperatura em Celsius e converte em Fahrenheit
c = float(input('Informe a temperatura em C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.1f}C comrresponde a {:.1f}F'.format(c, f))
