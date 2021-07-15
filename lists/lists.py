nome_paises = ['brazil', 'argentina', 'china', 'canada', 'japan']
print(nome_paises)

print("Tamanho da lista é", len(nome_paises))
print("País:", nome_paises[4])  # buscando japao
print("País:", nome_paises[-1])  # buscando japao

# sobreescrevendo na lista
nome_paises[2] = "russia"
print("País 3:", nome_paises[2])

# selecionando alguns
print(nome_paises[0:4], '         -- nome_paises[0:4]')
print(nome_paises[0:-1], '         -- nome_paises[0:-1]')
print(nome_paises[0:], '-- nome_paises[0:]')
print(nome_paises[:-1], '         -- nome_paises[:-1]')
print(nome_paises[:], '-- nome_paises[:]')

# por step
print(nome_paises[::2])  # de 2 em 2

# invertendo
print(nome_paises[::-1])

# searching
print("brazil" in nome_paises)  # resultado boolean
print("brazil" not in nome_paises)  # resultado boolean

################################################################

lista_capitais = []  # criar lista

lista_capitais.append('brasilia')  # add na lista
lista_capitais.append('buenos aires')
lista_capitais.append('roma')
lista_capitais.append('london')
lista_capitais.append('tokyo')
print(lista_capitais)

# add em determinada posição
lista_capitais.insert(2, 'paris')
print(lista_capitais)

# deleter elemento da lista
lista_capitais.remove('buenos aires')
print(lista_capitais)

# deletar por posição
removido = lista_capitais.pop(1)
print(lista_capitais, removido)
