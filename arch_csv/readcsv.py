import csv

with open('brasil_covid.csv', 'r', encoding='utf-8') as archive_csv:
    leitor = csv.reader(archive_csv)
    header = next(leitor)
    for line in leitor:
        if float(line[2]) > 1:
            print(line)

# OU

with open('brasil_covid.csv', 'r') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linhas = linha.split(',')
        print(linha)

##### ESCREVERRRRRRR ######
with open('user.csv', 'w', encoding='utf-8', newline='') as arq_users:
    escritor = csv.writer(arq_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['igor', 'bonato', 'igorzingamer@bol.com', 'emo'])
