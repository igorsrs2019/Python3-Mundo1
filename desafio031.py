#Este programa recebe a distancia da viagem e cobra R$0.50 por km, para distancia de ate 200km e para viagens mais longas R$0.45

d = float (input('Qual a distancia da viagem? '))
print ('Você esta prestes a comecar uma viagem de {}Km'.format(d))
preco = d * 0.50 if d <= 200 else d * 0.45
print ('E o preço da passagem será de R${:.2f}'.format(preco))