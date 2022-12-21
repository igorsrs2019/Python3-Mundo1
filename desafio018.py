#Este programa recebe o angulo e exibe o Seno, Cosseno e a Tangente
from math import sin, cos, tan, radians

angulo = float (input('Digite um angulo '))
seno = sin(radians(angulo))
print('O angulo {} tem o SENO de {:.2f} '.format(angulo, seno))
cosseno = cos(radians(angulo))
print ('O angulo {} tem o COSSENO {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem a TANGENTE {:.2f}'.format(angulo, tangente))