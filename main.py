from src.modules.readDF import readDf # Ler DataFremes
from src.modules.getUrlYT import getUrl # API do YouTube => Pegar url de vídeos do yt por titulo
from src.modules.downloadMusic import download # YouTubeDL => usando para baixar músicas
from src.modules.searchTopMusic import addOneMusic, addSearchAlbumsArtist, addTopCurrentTracks, addTopOldTracks # Busca na API do Spotify, top músicas de um artista
from src.modules.createPast import createPast # Cria pastas
from src.modules.setDF import setDF # Salva em um data frame
from datetime import datetime


def getCurrentYear():
    now = datetime.now()
    return now.strftime("%Y")


def main(nameAction, method = addOneMusic):
    
    if len(method(nameAction)) == 4:
        nameFunc, result, length, nameArtist = method(nameAction).values()
    else:
        nameFunc, result, length, nameArtist, nameAlbum = method(nameAction).values() # Pegando valores de uma função facture
        
        
    NAME_PAST = ''
    if nameFunc == 'addSearchAlbumsArtist':
        NAME_PAST = f'{nameArtist} (album) {nameAlbum}'
        createPast(NAME_PAST)
    elif nameFunc == 'addTopCurrentTracks':
        NAME_PAST = f'{nameArtist} (melhores {getCurrentYear()})'
        createPast(NAME_PAST)
    elif nameFunc == 'addTopOldTracks':
        NAME_PAST = f'{nameArtist} (melhores antigas)'
        createPast(NAME_PAST)
        
    setDF(result, length, nameArtist)

    DF_MUSICS = readDf('nome-musicas.txt')
    

    for i in range(0, length):
        nameArtist_nameMusic = DF_MUSICS.loc[i, 0].title()
        download(getUrl(nameArtist_nameMusic), NAME_PAST if nameFunc != 'addOneMusic' else '')
        i += 1
        
    
    
main('Maiara e Maraisa', addSearchAlbumsArtist)
main('Zé neto e Cristiano - largado as traças')
main('Cristiano Araújo', addTopOldTracks)
main('Bruno e Marrone', addTopCurrentTracks)
