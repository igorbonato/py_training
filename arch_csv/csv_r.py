# CSV
'''O formato CSV (Comma Separated Values, ou Valores Separados por Vírgula)
é um arquivo de texto que representa dados em forma de tabela de forma simples.

Cada linha do arquivo de texto é uma linha da tabela, e as colunas são separadas por vírgulas.'''

import csv
1, 2, 3, 4

5, 6, 7, 8

9, 10, 11, 12

'''Poderíamos manipular estes arquivos diretamente usando as funções de arquivo vistas anteriormente.
Um fator complicador é que o formato CSV não é bem padronizado: apesar do nome,
é normal que outros separadores sejam usados ao invés de vírgula, como ";",
para permitir que a vírgula seja usada em um campo. Idem para a separação entre linhas.
Existe um módulo em Python para manipular arquivos CSV que nos ajuda a tratar essas diferenças.
Todo programa que for utilizar o módulo CSV deverá importá-lo em seu início através do comando: import csv
'''

with open('tabelaExemplo.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';',
                          lineterminator='\n')  # criando um escritor
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # writerows escreve cada "sublista" da lista como uma linha
    escritor.writerows(lista)

with open('tabelaExemplo.csv', "r") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';',
                        lineterminator='\n')  # criando um leitor
    print("O conteúdo do arquivo é:")
    print(leitor)
    for linha in leitor:
        print(linha)

# DictReader e DictWriter
'''Podemos também trabalhar com dicionários, nos quais a primeira linha é lida como a chave e as
demais são os respectivos valores:'''


with open('email.csv', 'r') as emails:
    # a primeira linha é lida como um cabeçalho
    leitor = csv.DictReader(emails, delimiter=';')
    for linha in leitor:
        # podemos chamar um valor específico de cada linha pela chave no cabeçallho
        print(linha['Login email'])


with open('names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name']  # definimos o cabeçalho
    # especificamos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves)

    writer.writeheader()  # escrevemos o cabeçalho
    # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'})
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})
