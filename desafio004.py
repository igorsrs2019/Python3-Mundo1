# Este exercicio verifica o tipo de dados digitado e identifica as caracteristicas dele.
entrada = input('Digite alguma coisa ')
print(type(entrada))
print('Este valor {} é numerico?', entrada.isnumeric())
print('Todas as letra que foram digitadas sao maiuscula?', entrada.isupper())
print('Todos os caracteres digitados sao letras?', entrada.isalpha())
print('O valor digitado foi um espaco?', entrada.isspace())
print('Todos os caracteres estao em minusculo?',entrada.islower())
print('Esta capitalizada?', entrada.istitle())
 