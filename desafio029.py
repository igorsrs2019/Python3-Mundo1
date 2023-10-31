#Este programa solicita que o condutor insira a velocidade, e se caso a mesma passar de 80Km o condutor é multado em R$7,00 por KM.

velocidade = float (input('Qual é a velocidade atual do carro?: '))
print ('Tenha um bom dia! Dirija com segurança')
multa = (velocidade-80) * 7
if velocidade > 80:
    print('MULTADO! Voçê excedeu o limite permitido que é de 80Km/h')
    print ('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Esta dentro do limite de velocidade')
