from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy
import os
import sys
# import json

client_id = os.environ['CLIENT_ID_SP']
client_secret = os.environ['CLIENT_SECRET_SP']

client_credentials_manager = SpotifyClientCredentials(
  client_id=client_id, 
  client_secret=client_secret)


sp = spotipy.Spotify(
  client_credentials_manager = client_credentials_manager, 
  auth_manager = SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri='https://localhost:3000',
                scope='playlist-read-private'
              )
  )

def addTopCurrentTracks(nameArtist, amountMusics=30): # Melhores músicas atuais
  result = sp.search(q=f'This Is {nameArtist}', type='playlist', limit=3)

  for i, item in enumerate(result['playlists']['items']):
    playlistOficial = item['owner']['display_name']
    if playlistOficial == 'Spotify': # Verificar, si a playlist é da Spotify
      idPlaylist = result['playlists']['items'][i]['id'] # Pegando id Playlist
      if len(idPlaylist) > 0:
        TRACKS = sp.playlist_items(playlist_id=idPlaylist, fields='items(track(name))', limit=amountMusics)
        
        nameMusics = []
        for i in TRACKS['items']:
          nameMusics.append(nameArtist + ' - ' +  i['track']['name'])
        return {
          'nameFunc': addTopCurrentTracks.__name__,
          'result': nameMusics,
          'length': len(nameMusics),
          'nameArtist': nameArtist
        }
        
      else:
          print("Artista não encontrado")
          

def addTopOldTracks(nameArtist, amountMusics = 30): # Melhores músicas antigas
  RESULT = sp.search(q=f'{nameArtist} - Antigas', type='playlist', limit=1) # pegar id playlist
  
  ID_PLAYLIST = RESULT['playlists']['items'][0]['id'] # Pegando id Playlist
  if len(ID_PLAYLIST) > 0:
    TRACKS = sp.playlist_items(playlist_id=ID_PLAYLIST, fields='items(track(name))', limit=amountMusics)
    
    nameMusics = []
    for i in TRACKS['items']:
      nameMusics.append(nameArtist + ' - ' +  i['track']['name'])
    return {
      'nameFunc': addTopOldTracks.__name__,
      'result': nameMusics,
      'length': len(nameMusics),
      'nameArtist': nameArtist
    }
      
  else:
    print("Artista não encontrado")

  
  
#Buscar albums
def addSearchAlbumsArtist(nameArtist, recentAlbum = False):
  RESULT = sp.search(q=f'{nameArtist} - Antigas', type='artist', limit=1) # Pegar id artista
  ID_ARTIST = RESULT['artists']['items'][0]['id']
  
  RESULT = sp.artist_albums(artist_id=ID_ARTIST, album_type='album')
    
  
  albums = []
  for i, item in enumerate(RESULT['items']):
    albums.append([item['name'], item['release_date'], item['total_tracks'], item['external_urls']['spotify'], item['id']])
    print(f'\nÍNDICE: {i}')
    print(f"Nome: {albums[i][0]}\nData: {albums[i][1]}\nQtde de Músicas: {albums[i][2]}\nUrl Playlist: {albums[i][3]}")
    
    if recentAlbum:
      result = sp.album_tracks(album_id=albums[0][4]) # Pegando as faixas
      
      tracks = []
      for i in result['items']:
        tracks.append([i['name']])

        print('')
        print(i['name'] + '\n' + i['preview_url'])
        
        
      return {
      'nameFunc': addSearchAlbumsArtist.__name__,
      'result': tracks,
      'length': len(tracks),
      'nameArtist': nameArtist,
      'nameAlbum': albums[0][0]
    }
        
      
  # Mostrar Músicas de um album
  INDEX = int(input('Escolha o índice do album: \nR: '))
  
  result = sp.album_tracks(album_id=albums[INDEX][4]) # Pegando as faixas
  
  tracks = []
  for i in result['items']:
    tracks.append([i['name']])

    print('')
    print(i['name'])
    print(i['preview_url'])

  return {
    'nameFunc': addSearchAlbumsArtist.__name__,
    'result': tracks,
    'length': len(tracks),
    'nameArtist': nameArtist,
    'nameAlbum': albums[INDEX][0]
  }    
  
  

# Buscar músicas individuais

def addOneMusic(nameMusicArtist):
  
  # NAME_PAST = nameMusicArtist[:nameMusicArtist.index('-')]
  # pesquisar a música
  result = sp.search(q=nameMusicArtist, limit=1)['tracks']['items'][0]
    
  artists = []
  for name in result['artists']:
    artists.append(name['name'])
    

  nameMusic = result['name']  # nome da música

  artists = ', '.join(artists) # concatenar todos artistas separados por vingula
    
  
  """ response = input(f'Deseja adicionar {artists} - {nameMusic} \n[s, n]\nR: ').lower()
  if response == 's': """
  return {
    'nameFunc': addOneMusic.__name__, 
    'result': f'{artists} - {nameMusic}',
    'length': 1,
    'nameArtist': artists,
    'nameAlbum': None
  }
  """ else:
    return False """