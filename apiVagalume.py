from requests import get, exceptions
from tabulate import tabulate
import os


VAGALUME_KEY = os.environ['VAGALUME_API_KEY']

artista_qtdeMusica = []

# Adicionar músicas ao DataFreme
def addMusicasDf(listaMusicas):
  
  with open('nome-musicas.txt', 'a', encoding='utf-8') as arquivo:
        for musicas in listaMusicas:
          arquivo.write(str(musicas[0]) + '\n')


def buscarTopMusicas(artista, qtdeMusica):
    
  listaTopMusicas = []
  
  try:
    url = f'https://api.vagalume.com.br/search.art?apikey={VAGALUME_KEY}&q={artista}'
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

  addMusicasDf(listaTopMusicas)
  # return listaTopMusicas if listaTopMusicas != [] else f'Não encontramos {artista} na nossa base de dados!'

def addDadosMusica():
  
  while True:
    
    print('[p] => Proxima Etapa') if len(artista_qtdeMusica) > 0 else False
    nomeArtista = input('Nome do Artista/Banda: ').title().strip()
    if nomeArtista == 'P':
      if len(artista_qtdeMusica) > 0:
        print('========================================================================')
        addQtdeMusica()
        break
      else:
        print('Digite no Mínimo 1 Artista!')
  
    if nomeArtista != '':
      print('')
      artista_qtdeMusica.append([nomeArtista])
      print(len(artista_qtdeMusica))
      print(tabulate(artista_qtdeMusica, headers=['  Artista/Bandas  '], tablefmt='pretty', showindex=True))
      print('')
    else:
      print('')
      print('       Por Favor, Digite algum Nome!       ')
      print('')
  
  
def addQtdeMusica():
  
  qtdeArtistas = len(artista_qtdeMusica)

  i = 0
  while i < qtdeArtistas:
    
    while True:
      
      print('Tecla [ENTER] => 25 Músicas')
      qtdeMusicas = input(f'Quantidade de Músicas para ({artista_qtdeMusica[i][0]}) (MÁXIMO 25): ').strip()
      
      # Tratativa de erro => Estiver vazio ou maior que 25
      if qtdeMusicas == '':
        artista_qtdeMusica[i].append(25)
        print(tabulate(artista_qtdeMusica, headers=['Artistas/Bandas', "Quantidade de Músicas"], tablefmt='pretty', showindex=True))
        i += 1
        break
      else:
        qtdeMusicas = int(qtdeMusicas)
        if qtdeMusicas >= 1 and qtdeMusicas <= 25:
          artista_qtdeMusica[i].append(int(qtdeMusicas))
          print(tabulate(artista_qtdeMusica, headers=['artista_qtdeMusica/Bandas', "Qtde Músicas"], tablefmt='pretty', showindex=True))
          # print(artista_qtdeMusica)
          i += 1
          break
        else:
          print('')
          print('   No MÁXIMO 25 músicas!   ')

    print('=================================================================================')

  #Editar dados da tabela    
  while True:
    print('[s] => Sim')
    print('[n] => Não')
    respRenomear = input('Editar alguma Informação? Artista ou Quantidade de Musicas?\n R: ').lower().strip()
    if respRenomear == 's' or respRenomear == 'sim':
      
      numeroIndex = int(input(f'Número correspondente ao índice do Artista [0 á {len(artista_qtdeMusica) - 1}]: '))
      
      nomeTemp = artista_qtdeMusica[numeroIndex][0]
      qtdeTemp = artista_qtdeMusica[numeroIndex][1]
      
      print('')
      print(f'[enter] para manter o nome: {artista_qtdeMusica[numeroIndex][0]}')
      artista_qtdeMusica[numeroIndex][0] = input('Novo nome: ').title().strip()
      if artista_qtdeMusica[numeroIndex][0] == '':
        artista_qtdeMusica[numeroIndex][0] = nomeTemp
      print('')
      print(f'[enter] para manter a quantidade: {artista_qtdeMusica[numeroIndex][1]}')
      artista_qtdeMusica[numeroIndex][1] = input('Quantidade de Musicas: ').title().strip()
      if artista_qtdeMusica[numeroIndex][1] == '':
        artista_qtdeMusica[numeroIndex][1] = qtdeTemp
        
      print(tabulate(artista_qtdeMusica, headers=['  Artistas/Bandas  ', "  Quantidade de Músicas  "], tablefmt='pretty', numalign='right', showindex=True))
      print('')
    else:
      # Mudar a menssagem
      # import os
      mensagem = "Pressione Qualquer Tecla para Iniciar Busca de Músicas..."
      os.system(f'echo {mensagem} & pause >nul')

      # os.system('pause')
      i = 0
      while i < len(artista_qtdeMusica):
        buscarTopMusicas(artista_qtdeMusica[i][0], artista_qtdeMusica[i][1])
        i += 1
      
      break
      
