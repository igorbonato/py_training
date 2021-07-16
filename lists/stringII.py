cumprimento = "Olá, "
nome = 'Igor'
print(cumprimento + nome)
print(nome * 3)

name = 'Igor'
idade = 22
doenca = 'depressao'
print(nome, 'tem ' + str(idade) + ' anos e tem', doenca)
print('{} tem {} anos e tem {}'.format(nome, idade, doenca))  # easy
print(f'{nome} tem {idade} anos e tem {doenca}')

preco_gasosa = 3.476
print('o preço da gasolina subiu e esta R$ {:.2f}'.format(preco_gasosa))
