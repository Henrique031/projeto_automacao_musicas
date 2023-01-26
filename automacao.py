import pandas as pd  # Ler Arquivos
import pyautogui as gui  # Funçõse do teclado
import pyperclip as clip  # Copia oque está em
import time

altor = input("Deseja Inserir um Nome de um Altor? ").lower()
if (altor == "s" or altor == "sim"):
    altor = True
    nomeAltor = input("Nome do Altor: ").title()
else:
    altor = False
    

erro = False
try:
    blocoNotas = pd.read_csv(r"D:\\Riicky\\Music\\rascunho.txt",
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


def openEdge():
    gui.hotkey("win", "s")
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\grupoPesquisaWin.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.write("Microsoft Edge")
    time.sleep(0.3)
    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\casinhaEdge.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.hotkey("win", "up")


def openAC():
    time.sleep(0.3);
    gui.hotkey("win", "s")
    time.sleep(0.5);
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\grupoPesquisaWin.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.write("aTube Catcher")
    time.sleep(0.5)
    gui.press("enter")
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\barraAC.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(1)
    gui.hotkey("alt", "tab")


def findYT():
    time.sleep(1);
    gui.hotkey("alt", "d")
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\logoGPT.png',
                                       grayscale=True,
                                       confidence=0.6):
        time.sleep(0.3)
    gui.hotkey("alt", "d")
    clip.copy("https://www.youtube.com/")
    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
    gui.press("enter")


def firstMusic():
    while not gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\pesquisarYT.png',
        grayscale=True,
        confidence=0.6
    ):  # Carregar yt
        time.sleep(0.3)

    btPesquisa = gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\pesquisarYT.png',
        grayscale=True,
        confidence=0.6
    )
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
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\haYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)

    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
        time.sleep(0.3)
            
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\centroVideoYT.png', grayscale=True, confidence=0.2):
        time.sleep(0.3)
    urlVideo = gui.locateCenterOnScreen('src\\automacaoMusica\\img\\centroVideoYT.png', grayscale=True, confidence=0.2)
    gui.moveTo(urlVideo, duration=0.1)
    
    while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.3):
            time.sleep(0.3)
    time.sleep(2);
    gui.hotkey("ctrl", "c")  # copiar url do video
    time.sleep(0.3)
    gui.hotkey("alt", "tab")  # voltar ac
    time.sleep(0.3)
    while not gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\colarAC.png',
        grayscale=True,
        confidence=0.8
    ):
        time.sleep(0.3)
    btColar = gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\colarAC.png',
        grayscale=True,
        confidence=0.8
    )
    gui.click(btColar, )
    
    while not gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\BaixarAC.png',
        grayscale=True,
        confidence=0.8
    ):
        time.sleep(0.3);

    btBaixar = gui.locateCenterOnScreen(
        'src\\automacaoMusica\\img\\BaixarAC.png',
        grayscale=True,
        confidence=0.8
    )
    gui.click(btBaixar)
    while not gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\iniciarAC.png',
            grayscale=True,
            confidence=0.8
        ):
        time.sleep(0.3);
        
def restMusic():
    i = 1
    while (i < len(blocoNotas)):
        print(i+1)
        gui.hotkey("alt", "tab")  # Ir para yt
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        xYT = gui.locateCenterOnScreen('src\\automacaoMusica\\img\\xPesquisaYT.png', grayscale=True, confidence=0.6)
        x, y = xYT
        gui.click(x - 60, y)
        
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\pesquisarYT.png',grayscale=True,confidence=0.6):  # Carregar yt
            time.sleep(0.3)
        pesquisar = gui.locateCenterOnScreen('src\\automacaoMusica\\img\\pesquisarYT.png',grayscale=True,confidence=0.6)
        gui.click(pesquisar) # Botão de perquisa YT
        
        nomeMusica = blocoNotas.loc[i, 0]  # pegar segunda musica diante
        if altor == True:
            clip.copy(f"{nomeAltor} - {nomeMusica}")
        else:
            clip.copy(f"{nomeMusica}") # copiar musica
         
        time.sleep(0.3);
        gui.hotkey("ctrl", "v")  # colar musica
        time.sleep(0.3)
        gui.press("enter")  # enter
        time.sleep(0.3)
        # Copiar link do video
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\haYT.png', grayscale=True, confidence=0.8): # Carregar yt
            time.sleep(0.3)
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\casaInicioYT.png', grayscale=True, confidence=0.8):
            time.sleep(0.3)
            
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\centroVideoYT.png', grayscale=True, confidence=0.2):
            time.sleep(0.3)
        urlVideo = gui.locateCenterOnScreen('src\\automacaoMusica\\img\\centroVideoYT.png', grayscale=True, confidence=0.2)
        gui.moveTo(urlVideo, duration=0.1)
        
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\relogioAssistirMaisTardeYT.png', grayscale=True, confidence=0.3):
            time.sleep(0.3)
        time.sleep(2);
        gui.hotkey("ctrl", "c")
        time.sleep(0.3)
        # =========
        gui.hotkey("alt", "tab")  # Voltar para AC(aTubeCatcher)
        while not gui.locateCenterOnScreen('src\\automacaoMusica\\img\\atubeCatcher.png', grayscale=True, confidence=0.6):
            time.sleep(0.3)
        # Botões colar e baixar música
        while not gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\colarAC.png',
            grayscale=True,
            confidence=0.8
        ):
            time.sleep(1)
        btColar = gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\colarAC.png',
            grayscale=True,
            confidence=0.8
        )
        gui.click(btColar)
        time.sleep(0.3);
        
        while not gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\BaixarAC.png',
            grayscale=True,
            confidence=0.8
        ):
            time.sleep(0.3);

        btBaixar = gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\BaixarAC.png',
            grayscale=True,
            confidence=0.8
        )
        gui.click(btBaixar)
        
        contador = 0
        while not gui.locateCenterOnScreen(
            'src\\automacaoMusica\\img\\iniciarAC.png',
            grayscale=True,
            confidence=0.8
        ):
            
            time.sleep(0.3);
            contador += 1
            if contador == 3:
                break
        # ==============
        i += 1

createDesktop()
openEdge()
openAC()
findYT()
firstMusic()
restMusic()
