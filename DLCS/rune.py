import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

aviso = 1
print(aviso)

MANA_STATUS = (83, 80, 217)
REGION_BUF_BAR = (2392, 315, 107, 11)
REGION_AMULET = (2393, 185, 32, 32)
REGION_RING = (2393, 257, 32, 32)



def check_mana():
    print(f'checando mana...')
    if event_th.is_set():
        return
    if pg.pixel(2497, 160) != MANA_STATUS:
        if pg.pixel(2486, 160) != MANA_STATUS:
            pg.press('f')
    if event_th.is_set():
        return
    
    if pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90, region=REGION_BUF_BAR) != None:
        print('entrou eenenenene')
        counter = 0
        while counter < 5:
            if event_th.is_set():
                return
            print('comendo!')
            pg.press('u')
            counter += 1    
                   
def check_equip():
    print('checando equips!')
    if pg.locateOnScreen('imgs/ring_slot.png', confidence=0.90, region=REGION_RING) != None:
        if event_th.is_set():
            return
        print('colocando ring')
        pg.press('7')
        pg.sleep(0.2)
    pg.press('F1')
    pg.sleep(30)
    if event_th.is_set():
        return


def run():
    print('inicio')
    while True:
        if event_th.is_set():
            return
        check_mana()
        pg.sleep(0.2)
        if event_th.is_set():
            return
        check_equip()


def key_code(key):
    if key == keyboard.Key.home:
        event_th.set()
        return False
    elif key == keyboard.Key.insert:
        th_run.start()
           

global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listner:
    listner.join()