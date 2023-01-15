import pandas as pd #Ler Arquivos
import pyautogui as gui#Funçõse do teclado
import pyperclip as clip#Copia oque está em ""
import time


artista = input("Digite o Nome do Artista: ")

blocoNotas = pd.read_csv(r"D:\\musicas\\musicas_baixadas\\" + artista + "\\rascunho.txt", 
header=None, 
delimiter='/t',
engine='python',
)
# print(blocoNotas)
# caminho = "D:\\musicas\\musicas_baixadas\\" + artista

def pegarPosicaoMouse(num):
    time.sleep(num)
    print(gui.position())


def abrirAtubeCatcher():
    gui.press("win")
    time.sleep(2)
    gui.write("aTube Catcher")
    time.sleep(1)
    gui.press("enter")
    time.sleep(5)


def abrirEdgeNoYT():
    gui.press("win")
    time.sleep(3)
    gui.write("Microsoft Edge")
    time.sleep(2)
    gui.press("enter")
    time.sleep(4)
    gui.hotkey("ctrl", "t")
    time.sleep(4)
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(9)
    gui.click(x=430, y=131)
    time.sleep(3)


def baixarPrimeiraMusicaDoArtista():
    nomeMusica = blocoNotas.loc[0, 0]
    print(nomeMusica)
    clip.copy(f"{artista} - {nomeMusica}")
    gui.hotkey("ctrl", "v")
    gui.press("enter")
    time.sleep(2)
    #Copiar Url do Vídeo
    gui.rightClick(x=799, y=230)
    time.sleep(2)
    gui.click(x=892, y=378)
    #======================
    time.sleep(1)
    gui.hotkey("win", "tab")
    time.sleep(1)
    gui.hotkey('right')
    time.sleep(1)
    gui.hotkey("enter")
    time.sleep(1)
    #Botões colar e baixar música
    gui.click(x=776, y=200)
    time.sleep(0.5)
    gui.click(x=847, y=229)
    #==============
    time.sleep(4)
    
def baixarRestoDasMusicas():
    i = 1
    while (i < len(blocoNotas)): 
        gui.hotkey("alt", "tab") #Ir para yt
        time.sleep(0.3)
        gui.click(x=656, y=131) #Botão de perquisa YT
        # time.sleep(0.3)
        gui.hotkey("ctrl", "a") #Selecionar txt inteiro
        # time.sleep(3)
        nomeMusica = blocoNotas.loc[i, 0] #pegar segunda musica
        clip.copy(f"{artista} - {nomeMusica}") #copiar musica
        gui.hotkey("ctrl", "v") #colar musica
        # time.sleep(3)
        gui.press("enter") #enter
        time.sleep(5)
        #Copiar link do video
        gui.moveTo(x=453, y=309) #mause por cima
        time.sleep(0.2)
        gui.hotkey("ctrl", "c")
        # time.sleep(3)
        #========= 
        gui.hotkey("alt", "tab")#Voltar para AC(aTubeCatcher)
        time.sleep(0.2)
        #Botões colar e baixar música
        gui.click(x=776, y=200)
        time.sleep(1)
        gui.click(x=847, y=235)
        time.sleep(2)
        #==============
        i+=1


abrirAtubeCatcher()
abrirEdgeNoYT()
baixarPrimeiraMusicaDoArtista()
baixarRestoDasMusicas()

pegarPosicaoMouse(1)
pegarPosicaoMouse(5)

