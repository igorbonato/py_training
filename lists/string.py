frase = "\nIgor é mt burro e esta estudando \"muito\" todo dia\n"
print(frase)  # printa com aspas

nome = "Igor"
print(nome[0])
print(nome[:3])

# SPLIT
paises = 'brazil, argentina, china, canada, japan'
nome_paises = paises.split(", ")
print(nome_paises)  # separar por virgula

# STRIP
cabecalho = "            MENU PRINCIPAL"
print(cabecalho.strip())

nome_cidade = 'RiO gRanDE DO suL'
print(nome_cidade.title())  # Rio Grande Do Sul
print(nome_cidade.capitalize())  # Rio grande do sul
print(nome_cidade.lower())  # rio grande do sul
print(nome_cidade.upper())  # RIO GRANDE DO SUL

# EX 1:
pergunta = input("eu sou muito burro? ")
pergunta = pergunta.strip()
while pergunta.lower() != 'sim':
    print('errou, é sim')
    pergunta = input("eu sou muito burro? ")
print("ainda bem que sabe!\n")

# EX 2:
msg = "IGOR É MUITO BURRO"
igor_burro = 'IGOR' in msg
print(igor_burro)  # bool
