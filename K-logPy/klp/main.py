from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as pyt

datanow = datetime.now()
data = datanow.strftime('%d-%m')
save = r'C:\Users\arthu\Desktop\Save\Content_' + data + '/'

try:
    os.mkdir(save)
except:
    pass