import random
import os


pasta = r'E:'
numeros = random.sample(range(0, len(os.listdir(pasta))), len(os.listdir(pasta))) # randomizar sem repetir

i = 0
for nome_musica in os.listdir(pasta):
  caminho_antigo = os.path.join(pasta, nome_musica)
  # print(caminho_antigo)
  caminho_novo = os.path.join(pasta, f'{str(numeros[i])} - {nome_musica}')
  os.rename(caminho_antigo, caminho_novo)
  i += 1