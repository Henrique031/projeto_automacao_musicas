import pandas as pd
from requests import get, exceptions
from tabulate import tabulate
import os


def addArtista():
  artistas= []
  
  while True:
    
    print('[p] => Proxima Etapa') if len(artistas) > 0 else False
    nomeArtista = input('Nome do Artista/Banda: ').title().strip()
    if nomeArtista == 'P':
      if len(artistas) > 0:
        addQtdeMusica(artistas)
        break
      else:
        print('Digite no Mínimo 1 Artista!')
  
    if nomeArtista != '':
      print('')
      artistas.append([nomeArtista])
      print(len(artistas))
      print(tabulate(artistas, headers=['Artistas/Bandas'], tablefmt='pretty', showindex=True))
      print('')
    else:
      print('')
      print('       Por Favor, Digite algum Nome!       ')
      print('')
  
  
def addQtdeMusica(nomesArtista):
  
  nome_qtdeMusicas = nomesArtista
  qtdeArtistas = len(nome_qtdeMusicas)

  i = 0
  while i < qtdeArtistas:
    
    while True:
      
      print('')
      print('(MÁXIMO 25) \nTecla [ENTER] => 25 Músicas')
      qtdeMusicas = input(f'Quantidade de Músicas para {nomesArtista[i]}: ').strip()
      
      # Tratativa de erro => Estiver vazio ou maior que 25
      if qtdeMusicas == '':
        nome_qtdeMusicas[i].append(25)
        print(nome_qtdeMusicas)
        # print(tabulate(nome_qtdeMusicas, headers=['Artistas/Bandas', "Qtde Músicas"], tablefmt='pretty', showindex=True))
        i += 1
        break
      else:
        qtdeMusicas = int(qtdeMusicas)
        if qtdeMusicas >= 1 and qtdeMusicas <= 25:
          nome_qtdeMusicas[i].append(int(qtdeMusicas))
          # print(tabulate(nome_qtdeMusicas, headers=['Artistas/Bandas', "Qtde Músicas"], tablefmt='pretty', showindex=True))
          print(nome_qtdeMusicas)
          i += 1
          break
        else:
          print('')
          print('   No MÁXIMO 25 músicas!   ')

  editarDados()
  
      
      
      
def editarDados():
  print('')
  while True:
    print('[s] => Sim')
    print('[n] => Não')
    respRenomear = input('Editar alguma Informação? Artista ou Quantidade de Musicas? ').lower().strip()
    if respRenomear == 'n' or respRenomear == 'nao' or respRenomear == 'não':
      break
    else:
      numeroIndex = int(input(f'Número correspondente a linha do Artista [0 á {len(artista_qtdeMusicas) - 1}]: '))
      artista_qtdeMusicas[numeroIndex][0] = input('Novo nome: ').title().strip()
      print(tabulate(artista_qtdeMusicas, headers=['Artistas/Bandas', "Qtde Músicas"], tablefmt='pretty', numalign='right', showindex=True))




print('')

def buscarTopMusicas(artista, qtdeMusica):
  
  VAGALUME_API_KEY = os.environ('VAGALUME_API_KEY')
  
  listaTopMusicas = []

  
  while i < (len(artista)):
  
    try:
      url = f'https://api.vagalume.com.br/search.art?apikey={VAGALUME_API_KEY}&q={artista}'
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
          musicas.write(i[0].strip() + '\n')




# addAstistasDf()
        
# print(tabulate(listaTopMusicas))
