#Este programa recebe a distancia da viagem e cobra R$0.50 por km, para distancia de ate 200km e para viagens mais longas R$0.45

d = int (input('Qual a distancia da viagem? '))
if d <= 200:
    print('O valor cobrado é R${:.2f} '.format (d * 0.50))
else:
    print('O valor cobrado é R${:.2f}'.format(d * 0.45))    