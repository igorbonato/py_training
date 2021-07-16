dados_cidade = {
    'nome': 'Porto Alegre',
    'estado': 'RS',
    'area_km2': 1000,
    'populacao': 10.52
}
print(type(dados_cidade))
print(dados_cidade)

# add chaves no dict
dados_cidade['país'] = 'Brasil'
print(dados_cidade)

print(dados_cidade['nome'])  # acessar tal coisa

# alterar
dados_cidade['area_km2'] = 1500
print(dados_cidade)

# alterar apenas por CÓPIA
dados_cidade_2 = dados_cidade.copy()
dados_cidade_2['nome'] = 'Caxias do sul'
print(dados_cidade_2)
print(dados_cidade)

# concatenacao update
novos_dados = {
    'populacao em M': 12,
    'fundacao': '20/09/1500'
}
dados_cidade.update(novos_dados)
print(dados_cidade)

# METODO GET - none
print(dados_cidade.get('prefeito'))

print('------')
print(dados_cidade.keys())  # retorna uma lista de chaves de um dict
print('------')
print(dados_cidade.values())  # retorna uma lista de valores de um dict
print('------')
# retorna uma lista de tuplas (chave,valor) de um dict
print(dados_cidade.items())
