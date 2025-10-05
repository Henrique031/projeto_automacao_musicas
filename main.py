from src.components.readDF import read_df
from src.components.downloadMusic import ytdl
from src.components.getUrlYT import search_url, search_url_playlist


while True:
    print('(exit/e) PARA ENCERRAR!!!')
    ARTIST_OR_LINK = input('URL/Nome Música ou (1) Para ler Lista de Músicas: ')

    if ARTIST_OR_LINK == 'exit':
        break

    elif ARTIST_OR_LINK == '1':
        print('Download lista de Músicas')
        list_songs = read_df('nome-musicas.txt')
        for i in range(0, len(list_songs)): 
            nameArtist_nameMusic = list_songs.loc[i, 0].title()
            print(nameArtist_nameMusic)
            ytdl(search_url(nameArtist_nameMusic))

    elif 'youtube.com/playlist?list' in ARTIST_OR_LINK:
        print("Downlaad PlayList")
        search_url_playlist(ARTIST_OR_LINK)
        list_songs = read_df('nome-musicas.txt')
        for i in range(0, len(list_songs)): 
            nameArtist_nameMusic = list_songs.loc[i, 0].title()
            print(nameArtist_nameMusic)
            ytdl(nameArtist_nameMusic)


    elif 'www.youtube.com' in ARTIST_OR_LINK:    
        print('Download por link')
        ytdl(ARTIST_OR_LINK)

    else:
        print('Download por pesquisa')
        ytdl(search_url(ARTIST_OR_LINK))
        
        

# 'https://youtube.com/playlist?list=PL1FnxkW6uQINqVduXrNBRMvmhbFMDBDDk&si=kXgzixaAzQnEopwY'