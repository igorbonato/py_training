import requests
from bs4 import BeautifulSoup

#headers for be a nav#

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

players = ['messi', 'cristiano', 'neymar']

for player in players:
    i = requests.get(
        "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query="+player[0])
player_page = BeautifulSoup(i.content)
player_num = player_page.select(
    "td.hauptlink > a.spielprofil_tooltip tooltipstered > href")

# download page
objeto_response = requests.get(i, headers=headers)

page = BeautifulSoup(objeto_response.content, 'html.parser')
player_name = []
tag_player = page.find("h1", {"itemprop": "name"})
player_name.append(tag_player.text)
print(player_name)

numbers_player = []
games = page.find_all("td", {"class": "zentriert"})
goals = page.find_all("td", {"class": "zentriert"})
assists = page.find_all("td", {"class": "zentriert"})
numbers_player.append(games[0].text)
numbers_player.append(goals[1].text)
numbers_player.append(assists[2].text)
print(numbers_player)
