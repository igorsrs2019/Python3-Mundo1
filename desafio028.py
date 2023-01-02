# Este programa recebe um numero do usuario e verifica se o computador escolheu o mesmo.
import random

npessoa = int (input ('Bem vindo ao jogo! Digite um numero entre 1 e 5: '))
ncomputador  = random.randrange(5)
if npessoa == ncomputador:
    print ('Parabéns, o numero escolhido é {} '.format(ncomputador), 'Voce acertou!')
else:
    print ('O Computador venceu, o numero escolhido foi {} e voce digitou o {} '.format(ncomputador, npessoa, ))    

