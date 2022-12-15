# O programa recebe os dias de locacao e o KM rodado e informa quanto o usuario deve pagar.
# Levando em consideracao que a cada dia alugado é R$60,00 e cada KM é R$0.15
dia = int (input('Quantos dias o carro foi alugado? '))
km = float (input('Quantos KM rodados? '))
pago = (dia * 60) + (km * 0.15)
print(('Voce alugou o carro por {} dias e rodou {:.2f} km. O valor a pagar é R${:.2f}'.format(dia, km, pago)))