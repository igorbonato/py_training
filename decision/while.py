contador = 0

while contador < 10:
    contador += 1
    if contador == 1:
        print(contador, 'item limpo')
    else:
        print(contador, "itens limpos")

print("fim da repetiçao")

########################################################################


while True:
    if contador < 10:
        contador += 1
        if contador == 1:
            print(contador, 'item limpo')
        else:
            print(contador, "itens limpos")
    else:
        break

print("fim da repetiçao")

########################################################################


texto = input("Digite a sua senha: ")
while texto != 'igorburro':
    texto = input("senha invalida, tente novamente ")

print("acesso permitido!")

########################################################################


contador = 0

while contador < 10:
    contador += 1
    if contador == 1:
        continue
    print(contador, "itens limpos")

print("fim da repetiçao")

########################################################################

horario = int(input('Qual horario é agora? '))

# Testando a condição uma única vez com o if:
if 0 < horario < 6:
    print('Você está no horario da madrugada')
else:
    print('Você nao está no horario da madrugada')

# Testando a condição em loop com o while:
while 0 < horario < 6:
    print('Você está no horario da madrugada')
    horario = horario + 1  # horario += 1
else:
    print('Você nao está no horario da madrugada')

# O while permite continuar decrementando o número de pipocas até chegar em 0:
num_pipocas = int(input('Digite o numero de pipocas: '))

while num_pipocas > 0:
    print('O numero de pipocas é: ', num_pipocas)
    num_pipocas = num_pipocas - 1

########################################################################

# o exemplo abaixo não aceita um salário menor do que o mínimo atual:
salario = float(input('Digite seu salario: '))
while salario < 998.0:
    salario = float(input('Entre com um salario MAIOR DO QUE 998.0: '))
else:
    print('O salario que você entrou foi: ', salario)


# o exemplo abaixo só sai do loop quando o usuário digitar "OK":
resposta = input('Digite OK: ')
while resposta != 'OK':
    resposta = input('Não foi isso que eu pedi, digite OK: ')

########################################################################
