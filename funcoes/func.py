def hello():
    print("hey mundo!")


hello()


def calcula_media(v1, v2, v3):
    soma = v1 + v2 + v3
    media = soma/3
    return media


resultado = calcula_media(10, 5, 10)
print(resultado)

resultado = calcula_media(v1=9, v2=8, v3=7)
print(resultado)

# quebra de linha
print('igor é', end=' ')
print('mt burro')  # msm linha


def calcula_media2(v1=0, v2=0, v3=0):
    soma = v1 + v2 + v3
    media = soma/3
    return media


resultado = calcula_media2()
print(resultado)
