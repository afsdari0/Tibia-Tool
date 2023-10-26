import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

aviso = 1
print(aviso)

REGION_BUF_BAR = (2392, 315, 107, 11)


def check_fome():
    print(pg.locateOnScreen('imgs/buf_speed.png', confidence=0.90, region=REGION_BUF_BAR))
    print(pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90, region=REGION_BUF_BAR))
    if pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90, region=REGION_BUF_BAR) != None:
        print('entrou eenenenene')
        counter = 0
        while counter < 5:
            if event_th.is_set():
                return
            print('comendo!')
            pg.press('u')
            counter += 1


def run():
    print('inicio')
    while True:
        if event_th.is_set():
            return
        check_fome()
        if event_th.is_set():
            return


def key_code(key):
    if key == keyboard.Key.esc:
        event_th.set()
        return False
    elif key == keyboard.Key.insert:
        th_run.start()
           

global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listner:
    listner.join()