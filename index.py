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
        blocoNotas = pd.read_csv(r"D:\\Riicky\\music\\" + artista + "\\rascunho.txt",
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
    gui.hotkey("ctrl", "win", "d")  # Criar nova area de trabalho
    time.sleep(2)
    gui.press("win")
    time.sleep(1.5)
    gui.write("aTube Catcher")
    time.sleep(0.3)
    gui.press("enter")
    time.sleep(2)


def abrirEdgeNoYT():
    gui.press("win")
    time.sleep(1.5)
    gui.write("Microsoft Edge")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(6)
    gui.hotkey("win", "up")
    time.sleep(0.3)
    gui.hotkey("alt", "d")
    time.sleep(0.3)
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
    gui.press("enter")
    time.sleep(9)  # Carregar yt
    gui.click(x=430, y=131)  # Clikar na barra de pesquisa
    time.sleep(2)


def baixarPrimeiraMusicaDoArtista():
    nomeMusica = blocoNotas.loc[0, 0]
    # print(nomeMusica)
    clip.copy(f"{artista} - {nomeMusica}")
    gui.hotkey("ctrl", "v")
    gui.press("enter")
    time.sleep(3)
    # Copiar link do video
    gui.moveTo(x=453, y=309)  # mouse por cima do video
    time.sleep(0.2)
    gui.hotkey("ctrl", "c")  # copiar link do video
    time.sleep(0.3)
    # ==================
    gui.hotkey("alt", "tab")  # Voltar para atubeCatcher
    time.sleep(0.5)
    # Botões colar e baixar música
    gui.click(x=776, y=200)  # Botão colar aTubeCatcher
    time.sleep(0.5)
    gui.click(x=847, y=218)  # Botão baixar atubeCatcher
    # ==============
    time.sleep(2)


def baixarRestoDasMusicas():
    i = 1
    while (i < len(blocoNotas)):
        gui.hotkey("alt", "tab")  # Ir para yt
        time.sleep(0.5)
        gui.click(x=656, y=131)  # Botão de perquisa YT
        time.sleep(0.5)
        gui.hotkey("ctrl", "a")  # Selecionar todo texto
        nomeMusica = blocoNotas.loc[i, 0]  # pegar segunda musica diante
        clip.copy(f"{artista} - {nomeMusica}")  # copiar musica
        gui.hotkey("ctrl", "v")  # colar musica
        time.sleep(0.5)
        gui.press("enter")  # enter
        time.sleep(1.8)
        # Copiar link do video
        gui.moveTo(x=453, y=309)  # mause por cima
        time.sleep(0.3)
        gui.hotkey("ctrl", "c")
        time.sleep(0.5)
        # =========
        gui.hotkey("alt", "tab")  # Voltar para AC(aTubeCatcher)
        time.sleep(0.5)
        # Botões colar e baixar música
        gui.click(x=776, y=200)  # Botão colar atubeCatecher
        time.sleep(0.3)
        gui.click(x=847, y=235)  # Botão baixar atubeCatecher
        time.sleep(0.3)
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
    time.sleep(0.3)
    gui.hotkey("alt", "tab")
 


abrirAtubeCatcher()
abrirEdgeNoYT()
baixarPrimeiraMusicaDoArtista()
baixarRestoDasMusicas()
abrirExploradorDeArquivos()