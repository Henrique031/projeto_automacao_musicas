import pandas as pd
from requests import get, exceptions
from tabulate import tabulate


artista_qtdeMusicas = []
listaTopMusicas = []


def renomearArtista():
  numeroIndex = int(input(f'Número correspondente a linha do Artista [0 á {len(artista_qtdeMusicas) - 1}]: '))
  artista_qtdeMusicas[numeroIndex][0] = input('Novo nome: ').title()
  print(tabulate(artista_qtdeMusicas, headers=['Artistas/Bandas', "Qtde Músicas"], tablefmt='pretty', numalign='right', showindex=True))


while True:
  print('Adicione os nomes de UM ou MAIS artista ou banda\nou [N] para COMEÇAR DOWNLOADS')
  artista = input('Artista/Banda: ').title()
  if artista == 'N':
    break
  
  qtdeMusicas = input('Número de Músicas (MÁXIMO 25) ou tecla ENTER (PADRÃO 25): ')
  if qtdeMusicas == '':
    qtdeMusicas = 25
  else:
    qtdeMusicas = int(qtdeMusicas)
  if qtdeMusicas > 25:
    while True:
      print('No MÁXIMO 25 músicas')
      qtdeMusicas = input('Número de Músicas (MÁXIMO 25) ou enter (PADRÃO 25): ')
      if qtdeMusicas == '':
        qtdeMusicas = 25
        break
      else:
        qtdeMusicas = int(qtdeMusicas)
        if qtdeMusicas <= 25:
          break
        
  print('')
  artista_qtdeMusicas.append([artista, qtdeMusicas])
  print(tabulate(artista_qtdeMusicas, headers=['Artistas/Bandas', "Qtde Músicas"], tablefmt='pretty', showindex=True))
  print('')
  
  
while True:
  print('Deseja renomear algum nome de um ARTISTA ou BANDA? [s] [n]')
  respRenomear = input('r: ').lower()
  if respRenomear == 'n':
    break
  else:
    renomearArtista()

print('')

def pegarTopMusicas(artista, qtdeMusica):
  
  try:
    url = f'https://api.vagalume.com.br/search.art?apikey=cc8d49c02ec592e086b41c906bd97e0d&q={artista}'
    response = get(url).json()["response"]["docs"][0]["url"]
    response = get(f"https://www.vagalume.com.br{response}index.js").json()
  except exceptions.HTTPError as errh:
    print("http Error:", errh)
  except exceptions.ConnectionError as errc:
    print("Erro de conexão:", errc)
  except exceptions.Timeout as errt:
    print("Excesso de Tempo:", errt)
  except exceptions.RequestException as err:
    print("Algo deu Errado", err)

  limitMusica = 0
  for topMusicas in response["artist"]["toplyrics"]["item"]:
    listaTopMusicas.append([f'{artista} - {topMusicas["desc"]}'])
    limitMusica += 1
    if limitMusica == qtdeMusica:
      break
      
      
def addAstistasDf():
    with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        for i in listaTopMusicas:
          musicas.write(i[0] + '\n')

i = 0
while i < (len(artista_qtdeMusicas)):
  pegarTopMusicas(artista_qtdeMusicas[i][0], artista_qtdeMusicas[i][1])
  i+=1

addAstistasDf()
        
print(tabulate(listaTopMusicas))
