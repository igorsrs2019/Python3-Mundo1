#Este programa recebe um nome completo e exibe. O nome com todas as letras maiusculas, todas minusculas, mostra quantas letras tem todos os caracteres sem contar o espaco e quantas letras tem no primeiro nome.

nome = str (input ('Digite o primeiro nome: ')).strip()
print ('Seu nome em maisculas é {} '.format(nome.upper()))
print('Seu nome em minusculas é {} '.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
