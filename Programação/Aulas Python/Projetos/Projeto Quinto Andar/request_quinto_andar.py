import re
import requests
from bs4 import BeautifulSoup

link =input("Copie o link do anúncio? ")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")



metro_quadrado = site.find("p", class_="CozyTypography xih2fc EKXjIf Ci-jp3")
print('\nMetragem:',metro_quadrado.get_text())


aluguel = site.find("p", class_="CozyTypography xih2fc _72Hu5c wIyEP2 _8JKqPG r4Q8xM")
aluguel_formatado = (aluguel.get_text()[8:])
print('Aluguel:', aluguel_formatado)

publicado = re.compile(r"Publicado há \d+")
data_publicacao = site.find("span", string=publicado)
print('Data de publicação:', data_publicacao.text.strip()[13:])
