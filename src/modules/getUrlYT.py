from youtubesearchpython import VideosSearch


def getUrl(titleMusic):
    # Pesquisa por título
    VIDEO_ID = VideosSearch(titleMusic, limit = 1).result()['result'][0]['id']

    # Obtém o ID do vídeo
    return f'https://www.youtube.com/watch?v={VIDEO_ID}'

