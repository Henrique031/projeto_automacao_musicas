from requests import get, exceptions # Fazer requisições
from tabulate import tabulate # Deixar o print (saida do console) mais bonita
import os # Usar recursos do sistema operacional


# Chave da api do vagalume, salva em variáveis do ambiente
VAGALUME_KEY = os.environ['VAGALUME_API_KEY']

# Matriz que guardara o nome do artista e a qtde de músicas do artista
artist_amountSongs = []

# Guardara músicas encontradas pela api
listTopSongs = []


def searchTopSongs(artist, amountSongs):
  
  # Teste de erros:
  try:
    url = f'https://api.vagalume.com.br/search.art?apikey={VAGALUME_KEY}&q={artist}'
    response = get(url).json()["response"]["docs"][0]["url"]
    response = get(f"https://www.vagalume.com.br{response}index.js").json()
  except exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
  except exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
  except exceptions.Timeout as errt:
    print("Connection Timeout:", errt)
  except exceptions.RequestException as err:
    print("Something went Wrong", err)

  # Contador para limitar a busca com base na qtde de músicas
  cont = 0
  for bestMusics in response["artist"]["toplyrics"]["item"]:
    #Guardar o nome do artista em um array com o nome do artista e o nome da música
    listTopSongs.append([f'{artist} - {bestMusics["desc"]}'])
    cont += 1
    # Quando o contador for igual a qtde de músicas, o for para
    if cont == amountSongs:
      break

  
# Adicionar músicas ao DataFreme
def addMusicDf():
  # Abrir o DataFreme "nome-musicas.txt"
  with open('nome-musicas.txt', 'w', encoding='utf-8') as file:
    # Looping que salvará os dados da matriz que um DataFreme
    for music in listTopSongs:
      file.write(str(music[0]) + '\n')

def addDatesArtist():
  # Add os nomes dos Artistas/Bandas
  while True:
    # Mostra o bt de proximo, só quando o usuário já add um artista
    print('[p] => Proxima etapa') if len(artist_amountSongs) > 0 else False
    artistName = input('Nome do Artista/Banda: ').title().strip()
    # Se for igual a P, programa passa para a função qtde
    if artistName == 'P':
      # Só pode avançar sí, pelo menos 1 artista for setado
      if len(artist_amountSongs) > 0:
        print('========================================================================')
        # Encerrando ele inicia o looping de adicionar a qtde de músicas
        break
      else:
        print('Digite no Mínimo 1 Artista!')
    # Se for diferente de nulo, é porque é um nome válido
    if artistName != '':
      print('')
      artist_amountSongs.append([artistName])
      print(len(artist_amountSongs))
      print(tabulate(artist_amountSongs, headers=['  Artista/Bandas  '], tablefmt='pretty', showindex=True))
      print('')
    else:
      print('')
      print('       Por Favor, Digite um Nome!       ')
      print('')


  # Índice usado para add a qtde de músicas na matriz
  i = 0
  while i < len(artist_amountSongs):
    # Add qtde de Músicas para cada um dos Artistas, do 0 até o último artista
    while True:
      #Peguntar quantas músicas o usuário quer
      print('Tecla [ENTER] => 25 Músicas')
      amountMusics = input(f'Quantidade de Músicas para ({artist_amountSongs[i][0]}) (MÁXIMO 25): ').strip()
      
      # Tratativa de erro => Estiver vazio ou maior que 25, irá aparecer uma mensagem de erro
      if amountMusics == '':
        artist_amountSongs[i].append(25)
        print(tabulate(artist_amountSongs, headers=['Artistas/Bandas', "Quantidade de Músicas"], tablefmt='pretty', showindex=True))
        i += 1
        break
      else:
        # Converter qtde de musicas em inteiro, se não for vázio oque o usuário digitou
        amountMusics = int(amountMusics)
        # Só é permitido números entre 1 a 25
        if amountMusics >= 1 and amountMusics <= 25:
          # Guardar a qtde na matriz
          artist_amountSongs[i].append(int(amountMusics))
          print(tabulate(artist_amountSongs, headers=['artist_amountSongs/Bandas', "Qtde Músicas"], tablefmt='pretty', showindex=True))
          i += 1
          break
        else:
          print('')
          print('   No máximo 25 músicas!   ')

    print('=================================================================================')

  #Editar dados da tabela (Caso o usuário queira)
  while True:
    # Pegunta se o usuário quer alterar alguns dos dados (Nome do Artista ou Qtde de Músicas)
    print('[s] => Sim')
    print('[n] => Não')
    respRename = input('Editar alguma Informação? Artista ou Quantidade de Musicas?\n R: ').lower().strip()
    if respRename == 's' or respRename == 'sim':
      
      # Numero do index para a busca do artista 
      numIndex = int(input(f'Número correspondente ao índice do Artista [0 á {len(artist_amountSongs) - 1}]: '))
      
      #Nome Temporário do Artista
      nameTemp = artist_amountSongs[numIndex][0] 
      #Quantidade Temporário de Músicas
      amountTemp = artist_amountSongs[numIndex][1]
      
      # Digitar o novo nome, caso o usuário queira manter o nome, só apertar o enter
      print('')
      print(f'[enter] para manter o nome: {artist_amountSongs[numIndex][0]}')
      artist_amountSongs[numIndex][0] = input('Novo nome: ').title().strip()
      if artist_amountSongs[numIndex][0] == '':
        artist_amountSongs[numIndex][0] = nameTemp
      print('')

      # Pressionar enter, mantém a quantidade
      print(f'[enter] para manter a quantidade: {artist_amountSongs[numIndex][1]}')
      artist_amountSongs[numIndex][1] = input('Quantidade de Musicas: ').title().strip()
      if artist_amountSongs[numIndex][1] == '':
        artist_amountSongs[numIndex][1] = amountTemp
        
      # Mostrar na tela em forma de tabela (um print mais bonito)
      print(tabulate(artist_amountSongs, headers=['  Artistas/Bandas  ', "  Quantidade de Músicas  "], tablefmt='pretty', numalign='right', showindex=True))
      print('')
    else:
      # Mensagem personalizada do os.system
      mensagem = "Pressione Qualquer Tecla para Iniciar Busca de Músicas..."
      os.system(f'echo {mensagem} & pause >nul')

      #Chamar a função de buscar as melhores músicas de cada artista
      #Irá chamar a função com base no tanho da lista de artistas
      i = 0
      while i < len(artist_amountSongs):
        searchTopSongs(artist_amountSongs[i][0], artist_amountSongs[i][1])
        i += 1

      addMusicDf()
      break
      
