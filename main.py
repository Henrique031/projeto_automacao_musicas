from src.modules.readDF import readDf # Ler DataFremes
from src.modules.getUrlYT import getUrl # API do YouTube => Pegar url de vídeos do yt por titulo
from src.modules.downloadMusic import download, ytdl # YouTubeDL => usando para baixar músicas
from src.modules.searchTopMusic import addSearchAlbumsArtist, addTopCurrentTracks, addTopOldTracks # Busca na API do Spotify, top músicas de um artista
from src.modules.createPast import createPast # Cria pastas
from src.modules.setDF import setDF # Salva em um data frame
from datetime import datetime


def getCurrentYear(): #Pegando ano atual
    now = datetime.now()
    return now.strftime("%Y")


def TakingDataMusic():
    namesAndCategory = []
    i = 0
    while True:
        print('Digite "[START ou S]" para Começar')
        ARTIST = input('Nome do artista: ').title()
        if ARTIST == 'Start' or ARTIST == 'S':
            return namesAndCategory
        # ARTIST = 'Henrique e Juliano'
        namesAndCategory.append([ARTIST])
        print(namesAndCategory)
            
        print(f'\n1 = Albums\n2 = Mais Tocadas Atualmente\n3 - Melhores Antigas\n4 - Nome da Música\n')

        OPTIONS = int(input('Digite a Opção Desejada: '))  
        # OPTIONS = 'Henrique e Juliano'
        
        if OPTIONS == 1:
            namesAndCategory[i].append(1)
        elif OPTIONS == 2:
            namesAndCategory[i].append(2)
        elif OPTIONS == 3:
            namesAndCategory[i].append(3)
        elif OPTIONS == 4:
            namesAndCategory[i].append(4)
            MUSIC = input('Nome da Musica: ')
            ARTIST_MUSIC = f'{namesAndCategory[i][0]} - {MUSIC}'.replace('/', '-')
            namesAndCategory[i][0] = ARTIST_MUSIC
    
        i+=1
        
        
        
def downloadMusic(ARTIST, OPTIONS):
    
    NAME_PAST = ''
    if OPTIONS == 1:
        # Pegando dados como, MÚSICAS, QUANTIDADE, NOME DO ALBUM
       TRACKS, LENGTH, ALBUM  = addSearchAlbumsArtist(ARTIST).values()
    #    Substituindo a barra por um traço
       NAME_PAST = f'{ARTIST} ({ALBUM})'.replace('/', '-')
    #    Criando pasta
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
        TRACKS = [ARTIST]
        LENGTH = 1
    

    # função "setDF" Guardar músicas no bloco de notas
    setDF(TRACKS, LENGTH, ARTIST, album=True) if OPTIONS == 1 else setDF(TRACKS, LENGTH, ARTIST)

    # Ler bloco de notas
    DF_MUSICS = readDf('nome-musicas.txt')
    
    # Download das músicas
    for i in range(0, LENGTH if LENGTH else len(DF_MUSICS)): 
        nameArtist_nameMusic = DF_MUSICS.loc[i, 0].title()
        download(getUrl(nameArtist_nameMusic), NAME_PAST if OPTIONS <= 3 else '')
        
        
        
def main():
    
    #Matriz contendo nome da música, e sua opção. exemplo: 1->Album 2->Melhores antigas 3-> Mais tocadas
    songData = TakingDataMusic()
    
    i = 0
    while i <= len(songData) - 1:
        downloadMusic(songData[i][0], songData[i][1])
        i+=1
        
    
main()

