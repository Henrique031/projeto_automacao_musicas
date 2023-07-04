import pandas as pd

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
 

 
dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python')
nomeArtista = 'marilia mendonça'.title()
with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        i = 0
        while i < len(dfMusicas):
            nomeMusica = dfMusicas.loc[i, 0].title()
            musicas.write(f'{nomeArtista} - {str(nomeMusica)}\n')
            i +=1
