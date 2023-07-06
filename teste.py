# from tabulate import tabulate # Ver a saída mais organizada
from yt_dlp import YoutubeDL # Baixar videos yt 
from time import sleep
import threading as thr
# import pandas as pd   # Ler Arquivos (usado para ler um bloco de notas)
# import os # Recursos do sistema operacional 
# from pyautogui import *  # Funções do teclado (atalhos do teclado e escrever)
# from pyperclip import copy, paste  # Copia e cola
# from time import sleep # Fazer o programa esperar alguns segundos antes de continuar a execução

"""  
# Gerando acesso token para o uso da api do spotify
url = 'https://accounts.spotify.com/api/token'

data = {
  'grant_type': 'client_credentials',
  'client_id': '894f0272e3914f6990c92ab317992de0',
  'client_secret': '52d12e90189c4dc4bde7e65bfb1270e2'
}

response = requests.post(url, data=data)
access_token = response.json()['access_token']

# get
artist_id = '3p7PcrEHaaKLJnPUGOtRlT'
url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=br'
headers = {
  'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
artist_data = response.json()

jsonParsed = json.dumps(artist_data, indent=4)
# print(jsonParsed)
 """
 

 
""" dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python')
nomeArtista = 'marilia mendonça'.title()
with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        i = 0
        while i < len(dfMusicas):
            nomeMusica = dfMusicas.loc[i, 0].title()
            musicas.write(f'{nomeArtista} - {str(nomeMusica)}\n')
            i += 1
            i +=1
 """
 
"""  # Saber o tipo de dado em python
num = 0
num = int(input('Número: '))

print(type(num))  """

""" list = [['O mundo Parou', 25], ['Raídas', 23]]

def addAstistaDf():
    with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        for i in list:
          musicas.write(i[0])
          
addAstistaDf()

for i in list:
  print(i[0]) """
  
# links = [['https://www.youtube.com/watch?v=i5bA3llp1PM&pp=ygUHTyBob21lbQ%3D%3D'], 
# ['https://www.youtube.com/watch?v=aA9mmz508Ro&pp=ygUiV2hpdG5leSBIb3VzdG9uIC0gVHJ5IEl0IE9uIE15IE93bg%3D%3D'], 
# ['https://www.youtube.com/watch?v=bflUJjH-puo&pp=ygUaV2hpdG5leSBIb3VzdG9uIC0gVGhpcyBEYXk%3D'],
# ['https://www.youtube.com/watch?v=QgqKiniomI4&pp=ygUNTyBtdW5kbyBwYXJvdQ%3D%3D'],
# ['https://www.youtube.com/watch?v=hbM_njkSkIc&pp=ygUZdG9kYSB2ZXogcXVlIGV1IHRlIGJlaWphcg%3D%3D']]



def baixarMusicas(url):  
  ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'no_warnings': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
  }
    
  with YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
      
def download_audio_threaded(url):
    thread = thr.Thread(target=baixarMusicas, args=(url,))
    thread.start()
      
download_audio_threaded('https://www.youtube.com/watch?v=hbM_njkSkIc&pp=ygUZdG9kYSB2ZXogcXVlIGV1IHRlIGJlaWphcg%3D%3D')
      
i = 0
while i < 3:
  sleep(1)
  print(f"Segundos: {i}")
  i += 1
download_audio_threaded('https://www.youtube.com/watch?v=i5bA3llp1PM&pp=ygUHTyBob21lbQ%3D%3D')

i = 0
while i < 7:
  sleep(1)
  print(f"Horas: {i}")
  i += 1
download_audio_threaded('https://www.youtube.com/watch?v=aA9mmz508Ro&pp=ygUiV2hpdG5leSBIb3VzdG9uIC0gVHJ5IEl0IE9uIE15IE93bg%3D%3D')

i = 0
while i < 5:
  sleep(1)
  print(f"Minutos: {i}")
  i += 1
download_audio_threaded('https://www.youtube.com/watch?v=bflUJjH-puo&pp=ygUaV2hpdG5leSBIb3VzdG9uIC0gVGhpcyBEYXk%3D')


i = 0
while i < 3:
  sleep(1)
  print(f"Anos: {i}")
  i += 1
download_audio_threaded('https://www.youtube.com/watch?v=QgqKiniomI4&pp=ygUNTyBtdW5kbyBwYXJvdQ%3D%3D')





# Barra de Progresso
""" 
from tqdm import tqdm # Barra de progresso
import yt_dlp

ydl_opts = {
    'progress_hooks': [my_hook],
}

def my_hook(d):
    if d['status'] == 'downloading':
        pbar.update_to(d['_percent_str'])
    if d['status'] == 'finished':
        pbar.update_to(100)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    pbar = tqdm(total=100)
    ydl.download(['your_url_here'])

"""