import pandas as pd  # Ler Arquivos (usado para ler um bloco de notas)
import pyautogui as gui  # Funções do teclado (atalhos do teclado e escrever)
import pyperclip as clip  # Copia e cola
import time
from tabulate import tabulate
from yt_dlp import YoutubeDL
import os

# -*- coding: utf-8 -*-

links = [] # Usado para guardar links, para no final baixar musicas
nomeArtista = ''
nomePasta = ''

# Validar se o arquivo foi encontrado.
erro = False
try:
    dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python') # Criar um df (DataFrame)
except FileNotFoundError as e:
    print("O arquivo não foi encontrado :(")
    erro = True
    exit(1) # Encerrar o programa
except Exception as e: # Um erro incomum
    print("Ocorreu um Erro Desconhecido")
    erro = True
    exit(1) # Encerrar o programa
finally:
    print("Arquivo encontrado <3")
    print('Processando Qtde de Músicas.....')
    time.sleep(2)
    print(tabulate(dfMusicas))
    print(f'Quantidade de músicas: {len(dfMusicas)}')
    os.system('pause')
    


def addNomeAstista():
    nomeArtista = input("Nome do Autor: ").title()
    time.sleep(1)
    while True:
        addAstistaDf(nomeArtista)
        dfMusicas = pd.read_csv("nome-musicas.txt", header=None, delimiter='/t', engine='python')
        print(nomeArtista)
        print('Deseja renomear? [s]im [n]ao')
        respRenomearAutor = input('r: ').lower()
        if respRenomearAutor == 's':
            respRenomearAutor = True
            nomeArtista = input('Nome do altor: ').title()
        else:
            respRenomearAutor = False        
            print(tabulate(dfMusicas))
            break


def addAstistaDf(nomeArtista):
    with open('nome-musicas.txt', 'w', encoding='utf-8') as musicas:
        i = 0
        while i < len(dfMusicas):
            nomeMusica = dfMusicas.loc[i, 0].title()
            musicas.write(f'{nomeArtista} - {str(nomeMusica)}\n')
            i +=1
       

        
def criarPasta():
    if (respAstista): # Se tiver artista, ja vai criar a pasta com o nome do artista
        os.makedirs(f'D:\Lenda Viva\Music\{nomeArtista}') # Cria uma pasta no diretório escolhido
        print(f'Será salvo em: \n D:\Lenda Viva\Music\{nomeArtista}')
        os.system('pause')
    else: # Se não, ele vai escolher o nome da pasta
        nomePasta = input('Nome da pasta: ').title()
        os.makedirs(f'D:\Lenda Viva\Music\{nomePasta}') # Cria uma pasta no diretório escolhido
        while True:
            print(f'Será salvo em: \n D:\Lenda Viva\Music\{nomePasta}') # Mostrar o diretório
            respRenomearPasta = input("Deseja renomear a nome da pasta? [s]im [n]ão").lower()
            if respRenomearPasta == 's': 
                novoNomePasta = input('Nome da pasta: ').title()
                os.rename(f'D:\Lenda Viva\Music\{nomePasta}', f'D:\Lenda Viva\Music\{novoNomePasta}') # Remear uma pasta
                nomePasta = novoNomePasta
            else:
                break
     
print("Deseja Inserir um Altor? [s]im [n]ão ")
respAstista = input("r: ").lower()
if (respAstista == "s"):
    addNomeAstista()
else:
    respAstista = False
    

print('Deseja criar uma pasta? [s]im [n]ão')
respCriarPasta = input('r: ').lower()

if respCriarPasta == 's':
    criarPasta()
else:
    respCriarPasta = False
    print('Será salvo em: \n D:\Lenda Viva\Music\musicas-baixadas')
    os.system('pause')
    
    
        
def abrirEdgeAnonimo():
    gui.hotkey("ctrl", "win", "d", interval=0.5) # Eu criei um atalho para criar uma nova area de trabalho
    time.sleep(1)
    gui.hotkey("ctrl", "alt", "n", interval=0.5) # Eu criei um atalho para abrir o edge
    procurarCasinhaEdge()
    gui.hotkey("ctrl", "shift", "n", interval=0.5) # Criar uma nova pagina anonima
    procurarInPrivate()
    

#Procurar casinha do navegador para liberar continuação
def procurarCasinhaEdge():
    # seg = 0
    while not gui.locateCenterOnScreen('src\\img\\casinha-edge.png',
                                        grayscale=True,
                                        confidence=0.7):
        time.sleep(1)
        gui.hotkey('win', 'up',interval=0.5)
        time.sleep(1)
        gui.hotkey('win', 'd',interval=0.5)
        time.sleep(1)
        gui.hotkey('win', 'shift', 'm',interval=0.5)
        

def procurarInPrivate():
    while not gui.locateCenterOnScreen('src\\img\\in-private.png',
                                        grayscale=True,
                                        confidence=0.8):
        time.sleep(1)
        gui.hotkey('win', 'up')



# Entrar já pesquisando o nome da música no YouTube
def pesquisaRapida():
    gui.hotkey("alt", "d") # Barra de pesquisa do navegador
    time.sleep(0.3)
    gui.write('Y', interval=0.3) # Escrever Y para depois dar tab (pesquisa no YT rápida direto da barra de pesquisa)
    gui.hotkey('tab') # Ativar pesquisa rápida YT
    

def pegarNomeMusica(linhaMusica):
    # Pegar musicas do bloco de notas
    nomeMusica = dfMusicas.loc[linhaMusica, 0].title() # [Linha, Coluna]  # title() deixa a primeira letra em maiúsculo
    clip.copy(f"{nomeMusica}")

def colarMusicaDpsEnter():
    gui.hotkey("ctrl", "v") # Colar nome da musica na barra de pesquisa rápida
    time.sleep(0.5)
    gui.press("enter") # Enter para ir na musica desejada

def procurarImagensVideoYT():
    gui.hotkey('ctrl', '0') # Maximizar tela
    # Procurar imagem do nome "há" de no preview de um vídeo
    while not gui.locateCenterOnScreen('src\\img\\bt-atualizar-navegador.png', grayscale=True, confidence=0.7):
        time.sleep(1)
    time.sleep(0.5)
    while not gui.locateCenterOnScreen('src\\img\\logo-yt.png', grayscale=True, confidence=0.7):
        time.sleep(1)
    time.sleep(0.5)
    while not gui.locateCenterOnScreen('src\\img\\ha-yt.png', grayscale=True, confidence=0.8):
        time.sleep(1)   
    time.sleep(0.5)
    # Procurar imagem da casinha no YT
    while not gui.locateCenterOnScreen('src\\img\\casa-inicio-yt.png', grayscale=True, confidence=0.6):
        time.sleep(1)
    time.sleep(0.5)

        
def verificarVideoPatrocinio():
    # Procurando video anuncio
    
    seg = 2 # 2 segundo procurando videos de patrocínio 
    while not gui.locateCenterOnScreen('src\\img\\video-anuncio.png', grayscale=True, confidence=0.8):
        time.sleep(1)
        seg -= 1
        if (seg <= 0):# igual a zero é pq não achou
            break    
    if (seg > 0): # se for maior que zero é pq achou
        return True

    seg = 2
    while not gui.locateCenterOnScreen('src\\img\\video-patrocinado.png', grayscale=True, confidence=0.8):
        time.sleep(1)
        seg -= 1
        if (seg <= 0): # igual a zero é pq não achou
            break     
    if (seg > 0): # se for maior que zero é pq achou
        return True
        
    return False
        
def moverCopiarLink():
    videoPatrocinio = verificarVideoPatrocinio() # Tem video anuncio? True/False
    # Se for localizado video com patrocínio/anúncio
    print(f"Video com Anuncio?:  {videoPatrocinio}")
    if (videoPatrocinio):
        gui.moveTo(x=434, y=540, duration=0.3) # Clicar no centro do vídeo do YT
    else:
        while not gui.locateCenterOnScreen('src\\img\\centro-video-yt.png', grayscale=True, confidence=0.4):
            print('Centro do video sem anuncio')
            time.sleep(1)
        # Colocar o cursor em cima do vídeo
        urlVideo = gui.locateCenterOnScreen(
                            'src\\img\\centro-video-yt.png', grayscale=True, confidence=0.4)
        print(urlVideo)
        x, y = urlVideo
        
        gui.moveTo(x + 240, y + 140, duration=0.3) # Clicar no centro do vídeo do YT


def btDireito():    
    gui.rightClick() # Clica com botão direito
            
def procurarImagemOpcaoLink():
    # Procurar a botão de copiar link
    while not gui.locateCenterOnScreen('src\\img\\copiar-link-yt.png', grayscale=True, confidence=0.6):
        time.sleep(1)
    
# Clicar na opção de copiar link, após de clicar com botão direito do mouse
def clicarCopiarLink():
    procurarImagemOpcaoLink()
    btCopiarLink = gui.locateCenterOnScreen('src\\img\\copiar-link-yt.png', grayscale=True, confidence=0.6)
    gui.moveTo(btCopiarLink, duration=0.4)
    time.sleep(0.5)
    gui.click()
    
def salvarLink():
    links.append(str(clip.paste()))

    
def fecharPaginas():
    gui.hotkey('alt', 'f4')
    time.sleep(1)
    gui.hotkey('alt', 'f4')
    time.sleep(1)
    gui.hotkey('win', 'ctrl', 'f4') # Encerrar area de trabalho virtual

            
def baixarMusica():
    musicasComSucesso = 0
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'D:\Lenda Viva\Music\musicas-baixadas\%(title)s.%(ext)s',
    }
    
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
        musicasComSucesso += 1
        

    print('Downloads Finalizados com Sucesso!')
    print(f'{musicasComSucesso} Musicas Baixadas com Exito')
    time.sleep(1)
    if respCriarPasta:
        os.startfile(f'D:\Lenda Viva\Music\{nomePasta}') # Abrir gerenciador de arquivos no caminho especificado
    else:
        os.startfile(r'D:\Lenda Viva\Music\musicas-baixadas') # Abrir gerenciador de arquivos no caminho especificado
        
        

def main(nomeMusic):
    pesquisaRapida()
    pegarNomeMusica(nomeMusic)
    colarMusicaDpsEnter()
    procurarImagensVideoYT()
    moverCopiarLink() # Dps de validado se á video com patrocínio
    btDireito()
    clicarCopiarLink()
    salvarLink()
    
    
abrirEdgeAnonimo()

i = 0
while (i < len(dfMusicas)):
    main(i)
    i+= 1
    

fecharPaginas()
baixarMusica()





            
    
