#Este programa recebe o valor do produto e informa quanto o usuario vai pagar com 5% de desconto.
valor = float(input('Qual é o valor do produto: R$'))
valordesconto = valor - (valor * 5 / 100)
print('O produto que custava R${:.2f} com desconto de 5% vai sair R${:.2f}'.format(valor, valordesconto))