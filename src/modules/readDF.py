import pandas as pd   # Ler Arquivos (usado para ler um bloco de notas)
from tabulate import tabulate
import os


def readDf(source):
    try:
        df = pd.read_csv(source, # Destino do arquivo
                                header=None, # Sem cabeçalho
                                delimiter='/t', # Onde houver tabulação, será separado as linhas
                                engine='python' # Deixar explicito a engine ao pandas
                                ) # Criar um df (DataFrame)
    except FileNotFoundError as e:
        print("O arquivo não foi encontrado :(")
        exit(1) # Encerrar o programa
    except Exception as e: # Um erro incomum
        print("Ocorreu um Erro Desconhecido")
        exit(1) # Encerrar o programa
    finally:
        print("Arquivo encontrado <3")
        print(tabulate(df, showindex=False))
        print(f'Quantidade de músicas: {len(df)}')
        return df