#Este programa recebe um nome completo e exibe. O nome com todas as letras maiusculas, todas minusculas, mostra quantas letras tem todos os caracteres sem contar o espaco e quantas letras tem no primeiro nome.

nome = str (input ('Digite o primeiro nome: '))
print (nome.upper())
print(nome.lower())
print (len(nome.strip()))
lista = (nome.split())
print (len(lista[0]))
