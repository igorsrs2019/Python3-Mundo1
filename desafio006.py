# Este programa recebe um numero e exibe o dobro, triplo e a raiz quadrada
n = int(input('Digite um numero inteiro '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}. '.format(n,d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))
