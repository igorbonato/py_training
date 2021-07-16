import csv

header = ['nome', 'sobrenome']
dados = []
opt = input('o que deseja fazer?\n1- Cadastro\n0 - 1 Sair\n')
while opt != '0':
    nome = input('diga-me teu nome ')
    sobrenome = input('diga-me teu sobrenome ')
    dados.append([nome, sobrenome])
    opt = input('o que deseja fazer?\n1- Cadastro\n0 - 1 Sair\n')
print(dados)

with open('users.csv', 'w', newline='') as arqq_csv:
    writer = csv.writer(arqq_csv)
    writer.writerow(header)
    writer.writerows(dados)
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
