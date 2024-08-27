import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ

# Insira suas credenciais do Spotify
client_id = environ['CLIENT_ID_SP']
client_secret = environ['CLIENT_SECRET_SP']

# Autenticação usando as credenciais do cliente
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtendo um token de acesso válido
token_info = client_credentials_manager.get_access_token()
token = token_info['access_token']

print("Token de acesso gerado:", token)
