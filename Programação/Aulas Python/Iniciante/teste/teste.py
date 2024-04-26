import requests
from bs4 import BeautifulSoup

link = "https://www.quintoandar.com.br/imovel/894394218/alugar/apartamento-1-quarto-santa-cecilia-sao-paulo?from_route=%22condominium_page%22"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())

#titulo = site.find("title")
#print(titulo)

pesquisa = site.find("<p", class_="CozyTypography xih2fc _72Hu5c Ci-jp3")
print(pesquisa)


#<p class="CozyTypography xih2fc _72Hu5c Ci-jp3">R$&nbsp;1.263</p>