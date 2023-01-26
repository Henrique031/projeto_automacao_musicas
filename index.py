import pandas as pd  # Ler Arquivos
import pyautogui as gui  # Funçõse do teclado
import pyperclip as clip  # Copia oque está em ""
import time

while True:
    erro = False
    artista = input("Digite o Nome do Artista: ")
    print("Carregando...")
    time.sleep(1)
    try:
        blocoNotas = pd.read_csv(r"D:\\Riicky\\Music\\" + artista + "\\rascunho.txt",
                                 header=None,
                                 delimiter='/t',
                                 engine='python',
                                )
    except FileNotFoundError as e:
        print("O arquivo não foi encontrado :(")
        erro = True
    except Exception as e:
        print("Ocorreu um Erro Desconhecido")
        erro = True
    finally:
        if erro == False:
            print("Arquivo encontratrado :)")
            time.sleep(2)
    if erro == False:
        break


def abrirAtubeCatcher():
    gui.hotkey("win", "ctrl", "d")  # Criar nova area de trabalho
    time.sleep(1)
    gui.press("win")
    while not gui.locateCenterOnScreen('ima\\desligarWin.png', grayscale=True, confidence=0.6):
        time.sleep(0.5)
    gui.write("aTube Catcher")
    time.sleep(0.2)
    gui.press("enter")
    while not gui.locateCenterOnScreen('imagens\\atubeCatcher.png', grayscale=True, confidence=0.6):
        time.sleep(0.5)
        gui.click(x=730, y=431)


def abrirEdgeNoYT():
    gui.press("win")
    while not gui.locateCenterOnScreen('imagens\\desligarWin.png', grayscale=True, confidence=0.6):
        time.sleep(0.5)
    gui.write("Microsoft Edge")
    time.sleep(0.2)
    gui.press("enter")
    while not gui.locateCenterOnScreen('imagens\\casinhaEdge.png', grayscale=True, confidence=0.6): # Carregar yt
        time.sleep(0.5)
    gui.hotkey("win", "up")
    time.sleep(0.2)
    while not gui.locateCenterOnScreen('imagens\\atualizarEdge.png', grayscale=True, confidence=0.6): # Carregar yt
        time.sleep(0.3)
    gui.hotkey("alt", "d")
    time.sleep(0.5)
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(1)
    gui.hotkey("alt", "d")
    time.sleep(1)
    gui.hotkey("ctrl", "v")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(1)
    while not gui.locateCenterOnScreen('imagens\\pesquisarYT.png', grayscale=True, confidence=0.6): # Carregar yt
        time.sleep(0.3)
    time.sleep(0.5)
    gui.click(x=430, y=131)  # Clikar na barra de pesquisa
    time.sleep(0.2)


def baixarPrimeiraMusicaDoArtista():
    nomeMusica = blocoNotas.loc[0, 0]
    clip.copy(f"{artista} - {nomeMusica}")
    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
    gui.press("enter")
    time.sleep(2)
    # Copiar link do video
    gui.moveTo(x=453, y=309, duration=1.5)  # mouse por cima do video
    while not gui.locateCenterOnScreen('imagens\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.9): # Carregar yt
            time.sleep(0.3)
    gui.hotkey("ctrl", "c")  # copiar link do video
    time.sleep(0.5)
    # ==================
    gui.hotkey("alt", "tab")  # Voltar para atubeCatcher
    while not gui.locateCenterOnScreen('imagens\\atubeCatcherMenor.png', grayscale=True, confidence=0.6):
        time.sleep(0.5)
    # Botões colar e baixar música
    gui.click(x=776, y=200)  # Botão colar aTubeCatcher
    time.sleep(0.5)
    gui.click(x=847, y=218)  # Botão baixar atubeCatcher
    # ==============
    time.sleep(0.3)


def baixarRestoDasMusicas():
    i = 1
    while (i < len(blocoNotas)):
        print(i)
        gui.hotkey("alt", "tab")  # Ir para yt
        while not gui.locateCenterOnScreen('imagens\\casaInicioYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.5)
        gui.click(x=656, y=131)  # Botão de perquisa YT
        time.sleep(0.3)
        gui.hotkey("ctrl", "a")  # Selecionar todo texto
        time.sleep(0.3)
        nomeMusica = blocoNotas.loc[i, 0]  # pegar segunda musica diante
        clip.copy(f"{artista} - {nomeMusica}")  # copiar musica
        gui.hotkey("ctrl", "v")  # colar musica
        time.sleep(0.3)
        gui.press("enter")  # enter
        time.sleep(1)
        # Copiar link do video
        while not gui.locateCenterOnScreen('imagens\\haYT.png', grayscale=True, confidence=0.8): # Carregar yt
            time.sleep(0.3)
        gui.moveTo(x=453, y=309,duration=0.5)  # mause por cima
        while not gui.locateCenterOnScreen('imagens\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.9): # Carregar yt
            time.sleep(0.3)
        time.sleep(0.5)
        gui.hotkey("ctrl", "c")
        time.sleep(0.3)
        # =========
        gui.hotkey("alt", "tab")  # Voltar para AC(aTubeCatcher)
        while not gui.locateCenterOnScreen('imagens\\atubeCatcher.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        # Botões colar e baixar música
        gui.click(x=776, y=200)  # Botão colar atubeCatecher
        time.sleep(0.3)
        gui.click(x=847, y=235)  # Botão baixar atubeCatecher
        time.sleep(4)
        # ==============
        i += 1


def abrirExploradorDeArquivos():
    gui.hotkey("win", "e")  # abrir gerenciador de arquivos
    time.sleep(1.5)
    gui.hotkey("win", "up")
    time.sleep(0.5)
    gui.hotkey("ctrl", "l")  # ctrl + l barra de caminho de arquivos
    caminho = "D:\Riicky\Music\musicas_baixadas"
    clip.copy(caminho)  # Copiar caminho
    time.sleep(0.5)
    gui.hotkey("ctrl", "v")  # Colar
    time.sleep(0.5)
    gui.press("enter")  # Enter
    time.sleep(0.5)
    gui.hotkey("alt", "tab")
 


abrirAtubeCatcher()
''' abrirEdgeNoYT()
baixarPrimeiraMusicaDoArtista()
baixarRestoDasMusicas()
abrirExploradorDeArquivos() '''