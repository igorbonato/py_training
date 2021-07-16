# nomes_cidade = ['Porto Alegre', 'Londres', 'Tokyo', 'Paris']
# for nome in nomes_cidade:
#     print(nome)

# # # tupla
# # nomes_cidade = 'Porto Alegre', 'Londres', 'Tokyo', 'Paris'
# # for nome in nomes_cidade:
# #     print(nome)

# # # usando while
# # contador = 0
# # nomes_cidade = ['Porto Alegre', 'Londres', 'Tokyo', 'Paris']
# # while contador < len(nomes_cidade):
# #     print(nomes_cidade[contador])
# #     contador += 1

cidade = {
    'nome': 'Porto Alegre',
    'estado': 'rs',
    'pop': 12.2
}
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

# ALTERAR ELEMENTO NA LISTA
nomes_cidade = ['Porto Alegre', 'Londres', 'Tokyo', 'Paris']
for position in range(len(nomes_cidade)):
    nomes_cidade[position] = 'caxias do sul'
print(nomes_cidade)

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 10)))  # [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]
