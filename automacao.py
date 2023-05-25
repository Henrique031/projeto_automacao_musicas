import pandas as pd  # Ler Arquivos
import pyautogui as gui  # Funçõse do teclado
import pyperclip as clip  # Copia oque está em
import time

altor = input("Deseja Inserir um Altor [s, sim, n, nao]? ").lower()
if (altor == "s" or altor == "sim"):
    altor = True
    nomeAltor = input("Nome do Altor: ").title()
else:
    altor = False


erro = False
try:
    blocoNotas = pd.read_csv(r"D:\\Riichy\\Music\\rascunho.txt",
                             header=None,
                             delimiter='/t',
                             engine='python',)
except FileNotFoundError as e:
    print("O arquivo não foi encontrado :(")
    erro = True
    exit(1)
except Exception as e:
    print("Ocorreu um Erro Desconhecido")
    erro = True
    exit(1)
finally:
    if erro == False:
        print("Arquivo encontratrado :)")
        time.sleep(2)


def createDesktop():
    gui.hotkey("win", "ctrl", "d")  # Criar nova area de trabalho
    time.sleep(1)


def openVD(temp):
    time.sleep(temp)
    gui.hotkey("win", "s")
    time.sleep(1)
    while not gui.locateCenterOnScreen('src\\automacao\\img\\grupoPesquisaWin.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)

    gui.write("VDownloader", interval=0.3)
    time.sleep(1)

    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\logos_VD.png',
                                       grayscale=True,
                                       confidence=0.9):
        time.sleep(1)

    gui.hotkey("win", "up")
    time.sleep(1)


def openEdge():
    gui.hotkey("win", "s")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\grupoPesquisaWin.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.write("Microsoft Edge")
    time.sleep(0.3)
    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\casinhaEdge.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.hotkey("win", "up")


def findYT():
    time.sleep(1)
    gui.hotkey("alt", "d")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\casinhaEdge.png', grayscale=True, confidence=0.6):
        time.sleep(0.3)

    time.sleep(1.5)
    gui.hotkey("alt", "d")
    time.sleep(1)
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(1.5)
    gui.press("enter")


def firstMusic():
    time.sleep(2)
    while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.6):  # Carregar yt
        time.sleep(0.3)

    time.sleep(1)

    btPesquisa = gui.locateCenterOnScreen(
        'src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.6)

    gui.click(btPesquisa)
    nomeMusica = blocoNotas.loc[0, 0].title()
    if altor == True:
        clip.copy(f"{nomeAltor} - {nomeMusica}")
    else:
        clip.copy(f"{nomeMusica}")

    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
    gui.press("enter")
    # Carregar yt
    while not gui.locateCenterOnScreen('src\\automacao\\img\\haYT.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\centroVideoYT.png', grayscale=True, confidence=0.2):
        time.sleep(0.3)
    urlVideo = gui.locateCenterOnScreen(
        'src\\automacao\\img\\centroVideoYT.png', grayscale=True, confidence=0.2)
    gui.moveTo(urlVideo, duration=0.1)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.3):
        time.sleep(0.3)
    time.sleep(2)
    gui.hotkey("ctrl", "c")  # copiar url do video
    time.sleep(0.3)

    gui.hotkey("alt", "tab")  # voltar VD
    time.sleep(0.3)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\bt_baixar_VD.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)
    btBaixar = gui.locateCenterOnScreen(
        'src\\automacao\\img\\bt_baixar_VD.png', grayscale=True, confidence=0.8)
    gui.click(btBaixar)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\bt_baixar_iniciarDownload_VD.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)
    btBaixarIniciar = gui.locateCenterOnScreen(
        'src\\automacao\\img\\bt_baixar_iniciarDownload_VD.png', grayscale=True, confidence=0.8)
    gui.click(btBaixarIniciar)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\bt_salvar_VD.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)
    btSalvar = gui.locateCenterOnScreen(
        'src\\automacao\\img\\bt_salvar_VD.png', grayscale=True, confidence=0.8)
    gui.click(btSalvar)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\preparando_VD.png', grayscale=True, confidence=0.6):
        time.sleep(1)
    print(1)


def restMusic():
    i = 1
    while (i < len(blocoNotas)):
        time.sleep(1)

        gui.hotkey("alt", "tab")  # Ir para yt
        time.sleep(0.5)

        while not gui.locateCenterOnScreen('src\\automacao\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)
        while not gui.locateCenterOnScreen('src\\automacao\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        xYT = gui.locateCenterOnScreen(
            'src\\automacao\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6)
        x, y = xYT
        gui.click(x - 60, y)

        # Carregar yt
        while not gui.locateCenterOnScreen('src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        pesquisar = gui.locateCenterOnScreen(
            'src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.6)
        gui.click(pesquisar)  # Botão de perquisa YT

        nomeMusica = blocoNotas.loc[i, 0]  # pegar segunda musica diante
        if altor == True:
            clip.copy(f"{nomeAltor} - {nomeMusica}")
        else:
            clip.copy(f"{nomeMusica}")  # copiar musica

        time.sleep(0.3)
        gui.hotkey("ctrl", "v")  # colar musica
        time.sleep(0.3)
        gui.press("enter")  # enter
        time.sleep(0.3)
        # Copiar link do video
        # Carregar yt
        while not gui.locateCenterOnScreen('src\\automacao\\img\\haYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)
        while not gui.locateCenterOnScreen('src\\automacao\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)

        while not gui.locateCenterOnScreen('src\\automacao\\img\\centroVideoYT.png', grayscale=True, confidence=0.2):
            time.sleep(0.3)
        urlVideo = gui.locateCenterOnScreen(
            'src\\automacao\\img\\centroVideoYT.png', grayscale=True, confidence=0.2)
        gui.moveTo(urlVideo, duration=0.1)

        while not gui.locateCenterOnScreen('src\\automacao\\img\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.3):
            time.sleep(0.3)

        time.sleep(3)
        gui.hotkey("ctrl", "c")
        time.sleep(0.3)
        # =========
        gui.hotkey("alt", "tab")  # Voltar para VD(vdownloader)
        while not gui.locateCenterOnScreen('src\\automacao\\img\\slidebar_VD.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        # Botões colar e baixar música
        while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\bt_baixar_iniciarDownload_VD.png',
            grayscale=True,
            confidence=0.8
        ):
            time.sleep(1)
        btBaixar = gui.locateCenterOnScreen(
            'src\\automacao\\img\\bt_baixar_iniciarDownload_VD.png',
            grayscale=True,
            confidence=0.8
        )
        gui.click(btBaixar)
        time.sleep(0.3)

        while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\bt_salvar_VD.png',
            grayscale=True,
            confidence=0.8
        ):
            time.sleep(0.3)

        btSalvar = gui.locateCenterOnScreen(
            'src\\automacao\\img\\bt_salvar_VD.png',
            grayscale=True,
            confidence=0.8
        )
        gui.click(btSalvar)

        contador = 0
        while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\slidebar_top_VD.png',
            grayscale=True,
            confidence=0.6
        ):
            time.sleep(1)
            contador += 1
            if contador == 3:
                print("Não encontrado a imagem pronto VD")
                break
        # ==============

        print(i+1)
        i += 1


# createDesktop()
# openVD(5)
# openEdge()
# findYT()
# firstMusic()
# restMusic()
