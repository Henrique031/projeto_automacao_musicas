import pandas as pd  # Ler Arquivos
import pyautogui as gui  # Funçõse do teclado
import pyperclip as clip  # Copia oque está em
import time

print("Deseja Inserir um Altor? [s, sim, n, nao] ")
altor = input("R: ").lower()
if (altor == "s" or altor == "sim"):
    altor = True
    nomeAltor = input("Nome do Altor: ").title()
else:
    altor = False

print("VDownloader já aberto? [s, sim, n, nao] ")
abrirVD = input('R: ').lower()
if (abrirVD == 's' or abrirVD == 'sim'):
    abrirVD = True
else:
    abrirVD = False
    
    


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
        print("Arquivo encontrado :)")
        time.sleep(2)


def createDesktop():
    gui.hotkey("win", "ctrl", "d")  # Criar nova area de trabalho
    time.sleep(1)



def openVD():
    
    print('Abrir vd manual')
    time.sleep(1)
    gui.hotkey("win", "s")
    time.sleep(1)
    while not gui.locateCenterOnScreen(
        'src\\automacao\\img\\grupoPesquisaWin.png',        
        grayscale=True,
        confidence=0.6
        ):
        time.sleep(0.3)

    gui.write("VDownloader", interval=0.1)

    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\logos_VD.png',
                                    grayscale=True,
                                    confidence=0.9):
        time.sleep(1)

    gui.hotkey("win", "up")
    time.sleep(1)



def openVdIconesOcultos():
    print('Vd já aberto')
    while not gui.locateCenterOnScreen(
        'src\\automacao\\img\\setaCimaWin.png',
        grayscale=True,
        confidence=0.8
    ):
        time.sleep(1)

    print("Achou seta para cima")
    btSeta = gui.locateCenterOnScreen(
        'src\\automacao\\img\\setaCimaWin.png', grayscale=True, confidence=0.5)
    gui.click(btSeta)
    print('Clicou')

    while not gui.locateCenterOnScreen(
        'src\\automacao\\img\\iconeVD.png',
        grayscale=True,
        confidence=0.8
    ):
        time.sleep(1)
    print('Achou icone')

    iconeVD = gui.locateCenterOnScreen(
        'src\\automacao\\img\\iconeVD.png', grayscale=True, confidence=0.8)
    gui.click(iconeVD)
    time.sleep(0.5)
    gui.click(iconeVD)
    print('Clicou')
    

def openEdge():
    gui.hotkey("win", "s")
    while not gui.locateCenterOnScreen(
        'src\\automacao\\img\\grupoPesquisaWin.png',
        grayscale=True,
        confidence=0.6
    ):
        time.sleep(1)
    gui.write("Microsoft Edge")
    time.sleep(1)
    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\casinhaEdge.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(1)
    gui.hotkey("win", "up")
    time.sleep(1);
    gui.hotkey("ctrl", "shift", "n")
    while not gui.locateCenterOnScreen('src\\automacao\\img\\casinhaEdge.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(1)
    time.sleep(2);
    gui.hotkey("alt", "tab")
    time.sleep(1);
    gui.hotkey("alt", "f4")


# Entrar no YT
def findYT():
    time.sleep(1)
    while not gui.locateCenterOnScreen('src\\automacao\\img\\casinhaEdge.png', grayscale=True, confidence=0.6):
        time.sleep(1)
    print('Casinha edge')

    time.sleep(1.5)
    gui.hotkey("alt", "d")
    time.sleep(1)
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(0.5)
    gui.press("enter")


def firstMusic():
    print("Primeira musica")
    time.sleep(2)
    gui.hotkey("ctrl", "0")
    print('Deixou 100%')
    
    while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\logo-yt.png', grayscale=True, confidence=0.6):  # Carregar yt
        time.sleep(1)
    print("Achou a logo")
    
    while not gui.locateCenterOnScreen(
            'src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.5):  # Carregar yt
        time.sleep(1)
    print("Pesquisa Youtube")

    time.sleep(1)

    btPesquisa = gui.locateCenterOnScreen(
        'src\\automacao\\img\\pesquisarYT.png', grayscale=True, confidence=0.5)
    gui.click(btPesquisa)
    print('Clicou no botão de pesquisa yt')
    
    nomeMusica = blocoNotas.loc[0, 0].title()
    if altor:
        clip.copy(f"{nomeAltor} - {nomeMusica}")
    else:
        clip.copy(f"{nomeMusica}")

    time.sleep(1);
    gui.hotkey("ctrl", "v")
    time.sleep(1)
    gui.press("enter")
    # Carregar yt
    while not gui.locateCenterOnScreen('src\\automacao\\img\\haYT.png', grayscale=True, confidence=0.8):
        time.sleep(1)

    print('Há  YT')

    while not gui.locateCenterOnScreen('src\\automacao\\img\\casaInicioYT.png', grayscale=True, confidence=0.6):
        time.sleep(1)

    print('Casa inicio  YT')

    while not gui.locateCenterOnScreen('src\\automacao\\img\\centroVideoYTAtualizado.png', grayscale=True, confidence=0.2):
        time.sleep(1)

    print('Centro vídeo')

    urlVideo = gui.locateCenterOnScreen(
        'src\\automacao\\img\\centroVideoYTAtualizado.png', grayscale=True, confidence=0.2)
    gui.moveTo(urlVideo, duration=0.1)
    
    time.sleep(2)
    gui.rightClick(urlVideo)
    
    time.sleep(1)

    while not gui.locateCenterOnScreen('src\\automacao\\img\\copiar-link-yt.png', grayscale=True, confidence=0.6):
        time.sleep(1)
        
    btCopiarLink = gui.locateCenterOnScreen('src\\automacao\\img\\copiar-link-yt.png', grayscale=True, confidence=0.6)
    gui.moveTo(btCopiarLink, duration=0.5)
    gui.click(btCopiarLink)
    print("Copiou")
    
    
def VD():
    gui.hotkey("alt", "tab")  # voltar VD
    time.sleep(1)
    gui.hotkey("win", "up")
    

    while not gui.locateCenterOnScreen('src\\automacao\\img\\slidebar_VD.png', grayscale=True, confidence=0.6):
        time.sleep(1)
    print('Botão baixar')

    btBaixar = gui.locateCenterOnScreen(
        'src\\automacao\\img\\slidebar_VD.png', grayscale=True, confidence=0.6)
    gui.click(btBaixar)
    print('Clicou')

    while not gui.locateCenterOnScreen('src\\automacao\\img\\bt_baixar_VD.png', grayscale=True, confidence=0.8):
        time.sleep(1)
    print('Botão baixar começar')

    btBaixarIni = gui.locateCenterOnScreen(
        'src\\automacao\\img\\bt_baixar_VD.png', grayscale=True, confidence=0.8)
    gui.click(btBaixarIni)
    gui.click(btBaixarIni)
    print('Clicou')

    while not gui.locateCenterOnScreen('src\\automacao\\img\\bt_salvar_VD.png', grayscale=True, confidence=0.8):
        time.sleep(1)
    print('Botão Salvar')

    btSalvar = gui.locateCenterOnScreen(
        'src\\automacao\\img\\bt_salvar_VD.png', grayscale=True, confidence=0.8)
    gui.click(btSalvar)
    print('Clicou')

    contador = 1
    while not gui.locateCenterOnScreen('src\\automacao\\img\\preparando_VD.png', grayscale=True, confidence=0.5):
        print('Contador' + contador)
        time.sleep(1)
        contador1 += 1
        if contador == 6:
            break
    contador = 1

    print('Preparou')



def restMusic():
    i = 1
    while (i < len(blocoNotas)):
        print(len(blocoNotas))
        time.sleep(1)

        gui.hotkey("alt", "tab")  # Ir para yt
        time.sleep(0.5)

        while not gui.locateCenterOnScreen('src\\automacao\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6):
            time.sleep(1)

        xYT = gui.locateCenterOnScreen(
            'src\\automacao\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6
        )
        x, y = xYT
        gui.click(x - 60, y)

        while not gui.locateCenterOnScreen('src\\automacao\\img\\persquisaPosX.png', grayscale=True, confidence=0.6):
            time.sleep(1)
        pesquisar = gui.locateCenterOnScreen(
            'src\\automacao\\img\\persquisaPosX.png', grayscale=True, confidence=0.6)
        gui.click(pesquisar)  # Botão de perquisa YT

        nomeMusica = blocoNotas.loc[i, 0]  # pegar segunda musica diante
        if altor == True:
            clip.copy(f"{nomeAltor} - {nomeMusica}")
        else:
            clip.copy(f"{nomeMusica}")  # copiar musica

        time.sleep(1)
        gui.hotkey("ctrl", "v")  # colar musica
        time.sleep(1)
        gui.press("enter")  # enter
        time.sleep(1)
        # Copiar link do video
        # Carregar yt

        while not gui.locateCenterOnScreen('src\\automacao\\img\\centroVideoYTAtualizado.png', grayscale=True, confidence=0.2):
            time.sleep(1)
        urlVideo = gui.locateCenterOnScreen(
            'src\\automacao\\img\\centroVideoYTAtualizado.png', grayscale=True, confidence=0.2)
        gui.moveTo(urlVideo, duration=0.1)

        time.sleep(3)
        gui.hotkey("ctrl", "c")
        time.sleep(1)
        # =========
        VD()
        # ==============

        print(i+1)
        i += 1

if (not abrirVD):
    # createDesktop() 
    openVD()
else:
    openVdIconesOcultos()

openEdge()
findYT()
firstMusic()
VD()
# restMusic()
