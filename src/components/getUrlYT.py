from googleapiclient.discovery import build
import os


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


