# O programa solicita uma frase e informa a quantidade de vezes que a letra a aparece, em qual posicao aparece a primeira vez e em qual posicao aparece a ultima vez.

frase = str (input('Digite uma frase: '))
print ('A letra (a) aparecece {}'.format(frase.count('a')),'vezes nesta frase')
print ('A primeira vez que a letra (a) aparece na frase é na posicao {}'.format(frase.find('a')))
print ('A ultima vez que a letra (a) aparece na frase é na posicao {}'.format(frase.rfind('a')))