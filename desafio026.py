# O programa solicita uma frase e informa a quantidade de vezes que a letra a aparece, em qual posicao aparece a primeira vez e em qual posicao aparece a ultima vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print ('A letra (A) aparecece {}'.format(frase.count('A')),'vezes nesta frase')
print ('A primeira vez que a letra (A) aparece na frase é na posicao {}'.format(frase.find('A')+1))
print ('A ultima vez que a letra (A) aparece na frase é na posicao {}'.format(frase.rfind('A')+1))