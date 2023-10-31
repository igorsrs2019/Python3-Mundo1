# Este programa recebe 3 numeros e informa qual é o maior e qual é o menor


n1 =  int (input('Digite o primeiro numero: '))
n2 = int (input('Digite o segundo numero: '))
n3 = int (input('Digite o terceiro numero: '))

# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2 
if n3 < n2 and n3 < n1:
    menor = n3    

# Verificando quem é o maior

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
     maior = n3
print ('O menor valor digitado foi {}'.format(menor))
print ('O maior valor digitado foi {}'.format(maior))