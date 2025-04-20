import os

# Adicionar músicas ao DataFreme
def setDF(tracksName, length=0, nameArtist='', album=False):
  
  length = len(tracksName) if length < 0 else length

  if album == True:
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
      for music in tracksName:
        for i, tracks in enumerate(music):
          file.write(f'{tracks}')
          if i != length -1:
            file.write('\n')
  else:
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
        for i, music in enumerate(tracksName):
          file.write(f'{music}')
          if i != length -1:
            file.write('\n')
  