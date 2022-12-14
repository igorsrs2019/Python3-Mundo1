# Este programa recebe um valor inteiro, e exibe ele em metros, centimentros e milimetros
medida = float(input('Digite um numero '))
centimetros =  medida * 100
milimetros = medida * 1000
hectometro = medida * 100
print('A medida de {} comrresponde a '.format(medida))
print('{} cm'.format(centimetros))
print('{} mm'.format(milimetros))
print('{:0<5} hc'.format(hectometro))
