from googleapiclient.discovery import build # Usada para fazer requisição google
import os # Manipular o sistema operacional

# nomeMusica = input('Nome da música: ')

# Pegar o link de um vídeo do youtube, a partir de um titulo de um vídeo
def searchUrlVideoYT(musica):
    # Pegar o valor da chave da api em uma variável de um ambiente
    DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']
    
    # Instaciando a função build, com as credenciais 
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

    # Parâmetros de busca da api
    resultadoBusca = youtube.search().list(
        q=musica, # Titúlo do vídeo
        type='video', # Tipo: Vídeo
        part='id,snippet', # Dados
        maxResults=1 # No Maximo 1 item vai vim da busca
    ).execute()

    video_id = resultadoBusca['items'][0]['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'

    return video_url

# if __name__ == buscaUrlVideo():
#     resultado = buscaUrlVideo(nomeMusica)
