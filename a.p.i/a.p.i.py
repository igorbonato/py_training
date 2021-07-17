# Consumindo APIs em Python
'''
As APIs são meios de nos conectarmos a recursos na internet.
Portanto, já possuímos as ferramentas na mão desde os capítulos anteriores.
Você irá construir a lógica para decidir o que você irá buscar/consultar,
montará uma string seguindo o formato indicado pela documentação da API (como todos os exemplos deste capítulo).
Em seguida você tratará a resposta de acordo:'''

# Se for JSON, utilize o método json da própria requests.
# Se for CSV, utilize o módulo CSV estudado anteriormente.
# Se for XML, podemos utilizar o módulo BeautifulSoup, que não será estudado aqui.

'''Para outros formatos, provavelmente a solução mais fácil será baixar um módulo preparado para lidar com eles.
Descobrindo APIs: tem boas ideias e gostaria de saber se existe uma boa API para ajudar?
Confira alguns bons repositórios de API organizados por categoria:'''

# https://github.com/n0shake/public-apis

# https://github.com/public-apis/public-apis

# https://any-api.com/

'''Sites de governos costumam ter uma grande riqueza de dados também.
Segue abaixo algumas sugestões (oficiais ou mantidas por voluntários) com dados do Brasil como um todo.
Experimente buscar por bases de dados de sua cidade ou estado!'''

# http://www.transparencia.gov.br/swagger-ui.html

# http://www.dados.gov.br/

# https://brasil.io/home/


# URI base
'''Várias APIs fornecem um "endereço base". Todas as suas requisições incluirão esse endereço,
e ao final dele nós colocamos detalhes específicos para cada um dos recursos disponíveis.

Por exemplo, na AlphaVantage (https://www.alphavantage.co/),
uma API de dados de bolsas de valores e criptomoedas, a URI base é:'''

# https://www.alphavantage.co/query?

'''Após a interrogação nós colocaremos os campos para nossa consulta.
Por exemplo, para fazer uma consulta sem autenticação para valores da IBM, de 5 em 5 minutos, o endereço completo fica:
'''
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo

'''Note o formato com &NomeDoCampo=ValorDoCampo. Ele é bastante comum. Outro formato bastante comum é o de "subdiretórios".

Um exemplo é a PokéAPI. A URI base é:'''

# https://pokeapi.co/api/v2/

'''Para procurar por pokémons, adicionamos pokemon/.
Em seguida, podemos colocar números (índices) ou nomes de Pokémon, como:
'''
# https://pokeapi.co/api/v2/pokemon/ditto/

# https://pokeapi.co/api/v2/pokemon/25

'''Se ao invés de pokémons estivéssemos interessados em tipos de pokémon,
usaríamos types/ e o nome ou índice do tipo desejado:
'''
# https://pokeapi.co/api/v2/type/ghost
