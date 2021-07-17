import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
print(req.status_code)

dados = req.json()

print(dados)

valor_reais = float(input("informe o valor em reais a ser convertido\n"))
cotacao = dados['rates']['BRL']
print(f'R$ {valor_reais} em dólar valem US$ {(valor_reais / cotacao):.2f}')
