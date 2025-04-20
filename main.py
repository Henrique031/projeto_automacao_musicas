from src.components.readDF import read_df
from src.components.downloadMusic import download, ytdl
from src.components.getUrlYT import search_url


while True:
    print('(exit/e) PARA ENCERRAR!!!')
    ARTIST = input('URL/Nome Música ou (1) Para ler Lista de Músicas: ')
    if ARTIST == 'exit':
        break
    else:
        if 'www.youtube.com' in ARTIST:
            ytdl([ARTIST])
        elif '1' in ARTIST:
            list_songs = read_df('nome-musicas.txt')
            for i in range(0, len(list_songs)): 
                nameArtist_nameMusic = list_songs.loc[i, 0].title()
                download(search_url(nameArtist_nameMusic))
                
        else:
            ytdl([search_url(ARTIST)])

        print("Finalizado com Sucesso!!")