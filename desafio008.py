# Este programa recebe um valor inteiro, e exibe ele em metros, centimentros e milimetros
valor1 = int(input('Digite um numero'))
resultadoMetros = valor1 * 100
resultadoMilimetros = valor1 * 1000

print('O valor digitado é {} metros e {} centimetros e {} milimetros'.format(valor1, resultadoMetros, resultadoMilimetros))
