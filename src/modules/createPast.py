import os 
import shutil

def createPast(name):
  try:
    os.makedirs(f'D:\\henri\\Music\\musicas_baixadas\\{name}')
  except:
    print('Pasta já criada!! Foram removidos todos arquivos e pastas, e criado um nova pasta')
    shutil.rmtree(f'D:\\henri\\Music\\musicas_baixadas\\{name}') # Remove pasta, subpastas e arquivos
    os.makedirs(f'D:\\henri\\Music\\musicas_baixadas\\{name}')

    # D:\henri\Music