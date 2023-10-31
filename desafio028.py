from random import randint
from time import sleep


ncomputador  = randint(0, 5) # Faz o computador "PENSAR"
print ('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar ....')
print ('-=-' * 20)
npessoa = int (input ('Em que número eu pensei?? '))
print('PROCESSANDO...')
sleep(3)
if npessoa == ncomputador:
    print ('PARABÉNS! o numero escolhido é {} '.format(ncomputador), 'Voce acertou!')
else:
    print ('GANHEI!  o numero escolhido foi {} e voce digitou o {} '.format(ncomputador, npessoa, ))    

