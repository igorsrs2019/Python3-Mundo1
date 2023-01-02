# Este programa recebe o nome de uma Cidade e verifica se o primeiro nome é Santo

cidade = str(input('Digite uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

