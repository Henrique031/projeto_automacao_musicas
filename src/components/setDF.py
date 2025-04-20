import os

# Adicionar músicas ao DataFreme
def set_df(tracksName, length=0):
    tracksName = [tracksName]
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
        for i, music in enumerate(tracksName):
          file.write(f'{music}')
          if i != length -1:
            file.write('\n')