from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import os
import json

# Variavel de ambiente
API_KEY = os.environ['API_YT_KEY_1']

def search_url(nome_video, API_KEY = API_KEY):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        part='snippet',
        q=nome_video,
        maxResults=1
    )
    response = request.execute()
    return 'https://www.youtube.com/watch?v=' + response['items'][0]['id']['videoId']


def search_url_playlist(url, API_KEY = API_KEY):

    # Faz o parsing da URL
    parsed_url = urlparse(url)

    # Extrai os parâmetros da URL
    params = parse_qs(parsed_url.query)

    # Pega o valor do parâmetro 'list'
    PLAYLIST_ID = params.get('list', [None])[0]

    next_page_token = None
    total_videos = 0
    while True:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=PLAYLIST_ID,
            maxResults=50,  # máximo permitido por página
            pageToken=next_page_token,
        )

        response = request.execute()
        total_videos += len(response['items'])
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    links = []

    """ res = response['items'][0]['snippet']['resourceId']['videoId']
    json_formatado = json.dumps(res, indent=4, ensure_ascii=False)
    print(json_formatado) """


    for item in response['items']:
        titulo = item['snippet']['title']
        print(titulo + '\n')
        links.append('https://www.youtube.com/watch?v=' + item['snippet']['resourceId']['videoId'])   

    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
        for i,item in enumerate(links):
            file.write(item)
            if i != total_videos -1:
                file.write('\n')


