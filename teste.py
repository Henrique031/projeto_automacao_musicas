import pyautogui as gui
import time

location = gui.locateCenterOnScreen('print.png', grayscale=True) 
teste = True if location else False
print(teste)
    
# print(encontrou)location = gui.locateCenterOnScreen('print.png', grayscale=True)
# if location:
#     encontrou = True
#     print(location)
# else:
#     encontrou = False
#     print("tesdfds")
    
# print(encontrou)
    





# img1 = gui.locateAllOnScreen('print.png', grayscale=True)
# img1 = next(img1)
# gui.click(img1)
