# Este programa solicita seu nome completo e exibe ele com todas as letras maiusculas, todas em minusculas, conta quantos letras ele tem ao total e informa quantas letras tem o primeiro e informa o ultima nome e quantas letras tem.

nome = str (input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print ('Seu nome em maisculas é {} '.format(nome.upper()))   
print ('Seu nome em minusculas é {} '.format(nome.lower()))
print ('Seu nome tem ao todo {}'.format(len(nome.strip()))+ ' letras')
lista = (nome.split())
print ('Seu primeiro nome é {} e tem {}'.format(lista[0], len(lista[0]))+ ' letras')
print ('Seu ultimo nome é {} e tem {}'.format(lista[-1], len(lista[-1]))+ ' letras')