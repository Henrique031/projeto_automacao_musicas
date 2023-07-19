import pandas as pd   # Ler Arquivos (usado para ler um bloco de notas)
import os # Recursos do sistema operacional 
import threading as thr # Baixar músicas em segundo plano
from time import sleep # Fazer o programa esperar alguns segundos antes de continuar a execução
from tabulate import tabulate # Ver a saída mais organizada
from yt_dlp import YoutubeDL # Baixar videos yt
from googleapiclient.discovery import build # API YouTube
from requests import get, exceptions


nomeArtista = ''
nomePasta = ''


# Validar se o arquivo foi encontrado.
erro = False
try:
    dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python') # Criar um df (DataFrame)
except FileNotFoundError as e:
    print("O arquivo não foi encontrado :(")
    erro = True
    exit(1) # Encerrar o programa
except Exception as e: # Um erro incomum
    print("Ocorreu um Erro Desconhecido")
    erro = True
    exit(1) # Encerrar o programa
finally:
    print("Arquivo encontrado <3")
    print(tabulate(dfMusicas))
    print(f'Quantidade de músicas: {len(dfMusicas)}')
    os.system('pause')
    

def addNomeAstista():
    nomeArtista = input("Nome do Autor: ").title()
    sleep(1)
    while True:
        addAstistaDf(nomeArtista)
        dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python')
        print(nomeArtista)
        print('Deseja renomear? [s]im [n]ao')
        respRenomearAutor = input('r: ').lower()
        if respRenomearAutor == 's':
            respRenomearAutor = True
            nomeArtista = input('Nome do altor: ').title()
        else:
            respRenomearAutor = False        
            print(tabulate(dfMusicas))
            break


def addAstistaDf(nomeArtista):
    with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        i = 0
        while i < len(dfMusicas):
            nomeMusica = dfMusicas.loc[i, 0].title()
            musicas.write(f'{nomeArtista} - {str(nomeMusica)}\n')
            i +=1
       

def criarPasta():
    if (respAstista): # Se tiver artista, ja vai criar a pasta com o nome do artista
        os.makedirs(f'D:\Lenda Viva\Music\{nomeArtista}') # Cria uma pasta no diretório escolhido
        print(f'Será salvo em: \n D:\Lenda Viva\Music\{nomeArtista}')
        os.system('pause')
    else: # Se não, ele vai escolher o nome da pasta
        nomePasta = input('Nome da pasta: ').title()
        os.makedirs(f'D:\Lenda Viva\Music\{nomePasta}') # Cria uma pasta no diretório escolhido
        while True:
            print(f'Será salvo em: \n D:\Lenda Viva\Music\{nomePasta}') # Mostrar o diretório
            respRenomearPasta = input("Deseja renomear a nome da pasta? [s]im [n]ão").lower()
            if respRenomearPasta == 's': 
                novoNomePasta = input('Nome da pasta: ').title()
                os.rename(f'D:\Lenda Viva\Music\{nomePasta}', f'D:\Lenda Viva\Music\{novoNomePasta}') # Remear uma pasta
                nomePasta = novoNomePasta
            else:
                break
     
print("Deseja Inserir um Altor? [s]im [n]ão ")
respAstista = input("r: ").lower()
if (respAstista == "s" or respAstista == "sim"):
    addNomeAstista()    
else:
    respAstista = False
    

print('Deseja criar uma pasta? [s]im [n]ão')
respCriarPasta = input('r: ').lower()

if respCriarPasta == 's':
    criarPasta()
else:
    respCriarPasta = False
    print('Será salvo em: \n D:\Lenda Viva\Music\musicas-baixadas')
    sleep(1.5)    


def pegarNomeMusica(linhaMusica):
    # Pegar musicas do bloco de notas
    nomeMusica = dfMusicas.loc[linhaMusica, 0].title() # [Linha, Coluna]  # title() deixa a primeira letra em maiúsculo
    search_video_by_title(nomeMusica)

def search_video_by_title(title):
    
    DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    
    try:
        search_response = youtube.search().list(
            q=title,
            type='video',
            part='id',
            maxResults=1,
            fields='items(id(videoId))'
        ).execute()
    except exceptions.HTTPError as error:
        print(f'Um erro HTTP {error.resp.status} Causa: {error.content}')
    except Exception as error:
        print(f'Um erro ocorreu: {error}')
    else:
        video_id = search_response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
    # finally:
        # print('Musica baixada com sucesso')

    segundoPlanoDownloadMusica(video_url)

            
def downloadMusica(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        '--audio-format': 'best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'D:\Lenda Viva\Music\musicas-baixadas\%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
            
def segundoPlanoDownloadMusica(url):
    thread = thr.Thread(target=downloadMusica, args=(url,))
    thread.start()
        
        
def programaFinalizado():
    if respCriarPasta:
        os.startfile(f'D:\Lenda Viva\Music\{nomePasta}') # Abrir gerenciador de arquivos no caminho especificado
    else:
        os.startfile(r'D:\Lenda Viva\Music\musicas-baixadas') # Abrir gerenciador de arquivos no caminho especificado
            
    
i = 0
while (i < len(dfMusicas)):
    pegarNomeMusica(i)
    i+= 1
    

# programaFinalizado()
