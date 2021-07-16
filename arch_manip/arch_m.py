arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()

# while linha a linha
arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

# for linha a linha
arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

# sem close!
with open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)

###### CRIAR ARQUIVO  #######

with open('arquivo.texte.txt', 'w', encoding='utf-8') as archive:
    archive.write('primeira linha que estou escrevendo\n')
    archive.write('segunda linha que estou escrevendo, sou burro')

# add linha 'a'
with open('arquivo.texte.txt', 'a', encoding='utf-8') as archive:
    archive.write('\nadicinando linha')

with open('arquivo.texte.txt', 'r', encoding='utf-8') as archive:
    print(archive.read(), end='')
