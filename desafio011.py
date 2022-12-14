#Este programa recebe a largura e a altura da parede, informa a area e quantos litros de tinta sera necessario para pintar tudo.
#Levando em consideracao que a cada 2metros quadrados de parede precisa de 2 Litros e tinta.
largura = float(input('Digite a largura da parede '))
altura = float (input('Digite a altura da parede '))
area = largura * altura
tinta = area /2
print('A sua parede tem a dimensao de {:.2f}X{:.2f} e sua area é {:.2f}m2 \nPara pintar esta parede sera necessario {:.2f}l de tinta'.format(largura, altura, area, tinta))