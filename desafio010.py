#Este programa recebe um valor do usuario e exibe quantos dolares ele consegue comprar levando em consideracao
# A cotação atual R$1,00 = $3,27
valor = int(input('Digite um valor em R$ '))
dolar = (valor * 3,27)
print('Com esta quantia de R$ {} voce consegue comprar ${} dolares'.format(valor, dolar))