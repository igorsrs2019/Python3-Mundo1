#Este programa solicita que o condutor insira a velocidade, e se caso a mesma passar de 80Km o condutor é multado em R$7,00 por KM.

v = int (input('Digite a velocidade atual: '))
km = v - 80
m = km * 7 
if v > 80:
    print('A sua velocidade é de {}Km e voce foi multado em R${}'.format(v, m))
else:
    print('Esta dentro do limite de velocidade')
