# def calcula_media(v1, v2, v3):
#     soma = v1 + v2 + v3
#     media = soma/3
#     return media

def calcula_media(*args):  # o * identifica tupla
    soma = sum(args)
    media = soma / len(args)
    return media


result = calcula_media(10, 8, 9)
print(result)


def print_info(**kwargs):
    print(kwargs, type(kwargs))  # class dict


print_info(nome='Igor', sobrenome='Bonato')
