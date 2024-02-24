from src.modules.readDF import readDf # Ler DataFremes
from src.modules.getUrlYT import getUrl # API do YouTube => Pegar url de vídeos do yt por titulo
from src.modules.downloadMusic import download, ytdl # YouTubeDL => usando para baixar músicas
from src.modules.searchTopMusic import addOneMusic, addSearchAlbumsArtist, addTopCurrentTracks, addTopOldTracks # Busca na API do Spotify, top músicas de um artista
from src.modules.createPast import createPast # Cria pastas
from src.modules.setDF import setDF # Salva em um data frame
from datetime import datetime


def getCurrentYear(): #Pegando ano atual
    now = datetime.now()
    return now.strftime("%Y")


def main():
    
    # ARTIST = input('Nome do artista: ')
    ARTIST = 'Henrique e Juliano'
    print('')
    print(f'1 = Albums\n2 = Mais Tocadas Atuamente\n3 - Melhores Antigas\n4 - Nome da Música')
    print('')
    
    # OPTIONS = int(input('Digite a Opção Desejada: '))
    OPTIONS = 1
    NAME_PAST = ''
    if OPTIONS == 1:
       TRACKS, LENGTH, ALBUM  = addSearchAlbumsArtist(ARTIST).values()
       NAME_PAST = f'{ARTIST} ({ALBUM})'.replace('/', '-')
       createPast(NAME_PAST)
    elif OPTIONS == 2:
        TRACKS, LENGTH  = addTopCurrentTracks(ARTIST).values()
        NAME_PAST = f'{ARTIST} (Mais Tocadas De {getCurrentYear()})'.replace('/', '-')
        createPast(NAME_PAST)
    elif OPTIONS == 3:
        TRACKS, LENGTH = addTopOldTracks(ARTIST).values()
        NAME_PAST = f'{ARTIST} (Melhores Antigas)'.replace('/', '-')
        createPast(NAME_PAST)
    else:
        MUSIC = input('Nome da Musica: ')
        ARTIST_MUSIC = f'{ARTIST} - {MUSIC}'.replace('/', '-')
        TRACKS, LENGTH  = addOneMusic(ARTIST_MUSIC)
    
     # Criação de Pastas
    
    setDF(TRACKS, LENGTH, ARTIST, album=True) if OPTIONS == 1 else setDF(TRACKS, LENGTH, ARTIST)

    DF_MUSICS = readDf('nome-musicas.txt')
    
    for i in range(0, LENGTH if LENGTH else len(DF_MUSICS)): 
        nameArtist_nameMusic = DF_MUSICS.loc[i, 0].title()
        download(getUrl(nameArtist_nameMusic), NAME_PAST if OPTIONS <= 3 else '')
    
    
    
   
main()