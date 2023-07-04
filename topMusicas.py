import requests

artista = input('Artista/Banda: ').title()
print(f'Nome do Artista: {artista}')
print('Deseja renomear nome do artista/banda? [s] [n]')
respRenomear = input('r: ').lower()
if respRenomear == 's' or respRenomear != 'sim':
  while True:
    artista = input('Artista/Banda: ').title()
    print('Deseja renomear mais uma vez? [s] [n]')
    respRenomear = input('r: ').lower()
    print(f'Nome do Artista: {artista}')
    
    if respRenomear != 's' or respRenomear != 'sim':
      break

def pegarMelhoresMusicas(artista):
  # Pegar url do artista com o formato correto para usar na função listarMusicas()
  def pegarArtista(artista):
    url = f'https://api.vagalume.com.br/search.art?apikey=cc8d49c02ec592e086b41c906bd97e0d&q={artista}'
    return requests.get(url).json()["response"]["docs"][0]["url"]
    
    
  def listarMusicas(artista):
    artistaUrl = pegarArtista(artista)
    url = f"https://www.vagalume.com.br{artistaUrl}index.js"
    try:
      response = requests.get(url).json()
      for music in response["artist"]["toplyrics"]["item"]:
        print(f'{artista} - {music["desc"]}')
    except requests.exceptions.HTTPError as errh:
      print("http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
      print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
      print("Excesso de Tempo:", errt)
    except requests.exceptions.RequestException as err:
      print("Algo deu Errado", err)
        
      

    # except:
      
  listarMusicas(artista)
  
pegarMelhoresMusicas(artista)