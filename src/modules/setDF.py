import os

# Adicionar músicas ao DataFreme
def setDF(dateMusics, length=0, nameArtist='', album=False):
  
  length = len(dateMusics) if length < 0 else length

  if isinstance(dateMusics, list) and album == True:
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
      for music in dateMusics:
        for i, tracks in enumerate(music):
          file.write(f'{tracks}')
          if i != length -1:
            file.write('\n')
  elif isinstance(dateMusics, list) and album == False:
    
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
        for i, music in enumerate(dateMusics):
          file.write(f'{music}')
          if i != length -1:
            file.write('\n')
  elif isinstance(dateMusics, str):
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
      # Verificar se a pasta está vazia
      file.write(dateMusics) if os.stat('nome-musicas.txt').st_size == 0 else file.write(f'\n{dateMusics}')
  else:
    
    nomes = [item[0] for item in dateMusics] # list comprehension

    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
    # Looping que salvará os dados da matriz que um DataFreme
      for i, music in enumerate(nomes):
        file.write(f'{nameArtist} - {music}')
        if i != length -1:
          file.write('\n')
  
  """ 
  
  elif isinstance(dateMusics, list):
    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
      for i, music in enumerate(dateMusics):
        file.write(f'{music}')
        if i != length -1:
          file.write('\n')
  else:
    
    nomes = [item[0] for item in dateMusics] # list comprehension

    with open('nome-musicas.txt', 'w+', encoding='utf-8') as file:
    # Looping que salvará os dados da matriz que um DataFreme
      for i, music in enumerate(nomes):
        file.write(f'{nameArtist} - {music}')
        if i != length -1:
          file.write('\n') """
    