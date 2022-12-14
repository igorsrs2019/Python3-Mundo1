#Este programa recebe duas notas e exibe a média
n1 = float (input('Digite a sua primeira nota '))
n2 = float (input('Digite a segunda nota '))
m = ((n1 + n2) /2)
print('A media entre {:.1f} e {:.1f} é {:.1f}'.format(n1,n2, m))