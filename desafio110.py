# O programa solicita o valor do produto e informa o preco que seria com desconto de 8% para quem compra a vista.
valor = float (input('Digite o valor do produto R$ '))
valordesconto = valor - (valor * 8 /100)
print('O preco do valor a vista é R$ {} o preco do valor parcelado é R${} '.format(valordesconto, valor))