#Este programa recebe um valor em R$ do usuario e exibe quanto que ele consegue comprar em (Dolar, Euro e JPY)
# A cotação atual R$1,00 = 3.27 Dolares
# A cotacao atual R$1,00 = 5.27 Euro
# A cotacao atual R$1,00 = 421.00 JPY
real = float(input('Digite um valor em R$ '))
dolar = (real / 3.27)
euro = (real /5.27)
jpy = (real /421.00)
print('Com esta quantia de R${:.2f}'.format(real))
print('Voce consegue comprar $ {:.2f}'.format(dolar))
print('Voce consegue comprar Euro {:.2f}'.format(euro))
print('Voce consegue comprar jpy {:.2f}'.format(jpy))


