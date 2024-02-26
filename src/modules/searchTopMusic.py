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

def addTopCurrentTracks(nameArtist, amountMusics=10): # Melhores músicas atuais
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
          'result': nameMusics,
          'length': len(nameMusics),
        }
        
      else:
          print("Artista não encontrado")
          

def addTopOldTracks(nameArtist, amountMusics = 20): # Melhores músicas antigas
  RESULT = sp.search(q=f'{nameArtist} - Antigas', type='playlist', limit=1) # pegar id playlist
  
  ID_PLAYLIST = RESULT['playlists']['items'][0]['id'] # Pegando id Playlist
  if len(ID_PLAYLIST) > 0:
    TRACKS = sp.playlist_items(playlist_id=ID_PLAYLIST, fields='items(track(name))', limit=amountMusics)
    
    nameMusics = []
    for i in TRACKS['items']:
      nameMusics.append(nameArtist + ' - ' +  i['track']['name'])
    return {
      'result': nameMusics,
      'length': len(nameMusics),
    }
      
  else:
    print("Artista não encontrado")

  
  
#Buscar albums
def addSearchAlbumsArtist(nameArtist):
  RESULT = sp.search(q=f'{nameArtist} - Antigas', type='artist', limit=1) # Pegar id artista
  ID_ARTIST = RESULT['artists']['items'][0]['id']
  
  RESULT = sp.artist_albums(artist_id=ID_ARTIST, album_type='album')
    
  # Mostrar albums
  albums = []
  for i, item in enumerate(RESULT['items']):
    albums.append([item['name'], item['release_date'], item['total_tracks'], item['external_urls']['spotify'], item['id']])
    print(f'\nÍNDICE: {i}')
    print(f'Nome: {albums[i][0]}')
    print(f'Data: {albums[i][1]}')
    print(f'Qtde de Músicas: {albums[i][2]}')
    # print(f'Url Playlist: {albums[i][3]}')
    
  
  # Mostrar Músicas de um album
  INDEX = int(input('Escolha o índice do album: \nR: '))
  
  result = sp.album_tracks(album_id=albums[INDEX][4]) # Pegando as faixas
  
  tracks = []
  for i in result['items']:
    tracks.append([f'{nameArtist} ({albums[INDEX][0]}) - {i['name']}'])
    print('')
    print(i['name'])

  return {
    'result': tracks,
    'length': len(tracks),
    'nameAlbum': albums[INDEX][0]
  }    
  
