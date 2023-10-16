print('-='*20)
print ('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
a = float (input('Primeiro Seguimento: '))
b= float (input('Segundo seguimento: '))
c = float (input('Segundo seguimento: '))
#resultado = b + c
if (a < b + c) and  (b < a + c) and (c < a + b):
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:     
    print ('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')

