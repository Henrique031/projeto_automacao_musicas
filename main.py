from addNameMusicDF import addDatesArtist # API do vagalume => buscar as top músicas de um artira no df
from getUrlYTByTitle import searchUrlVideoYT # API do YouTube
from downloadSongs import downloadSongs # YouTubeDL => usando para baixar músicas
from readDF import readDf # Ler DataFremes
import testeOop as oop


topMusicas = oop.Artista()
topMusicas.addNameArtista()
print(topMusicas.getNameArtista())
# readDf('nome-musicas.txt')