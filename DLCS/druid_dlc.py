import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

aviso = 1
print(aviso)

LIFE_STATUS = (218, 79, 79)
FULL_LIFE_STATUS = (218, 79, 79)
HEAL_FRIEND = (74, 74, 74)
MANA_STATUS = (83, 80, 217)
REGION_BUF_BAR = (2392, 315, 107, 11)
REGION_AMULET = (2393, 185, 32, 32)
REGION_RING = (2393, 257, 32, 32)



def check_status(name):
    if name == 'life':
        print(f'checando {name}...')
        if event_th.is_set():
            return
        if pg.pixel(2497, 147) != FULL_LIFE_STATUS:
            if pg.pixel(2446, 147) != LIFE_STATUS:
                pg.press('3')
            elif pg.pixel(2474, 147) != LIFE_STATUS:
                pg.press('2')
            elif pg.pixel(2485, 147) != LIFE_STATUS:
                pg.press('1')
    elif name == 'mana':  
        print(f'checando {name}...')
        if event_th.is_set():
            return
        if pg.pixel(2497, 160) != MANA_STATUS:
            if pg.pixel(2486, 160) != MANA_STATUS:
                pg.press('f')
    if pg.pixel(460, 55) == HEAL_FRIEND:
        pg.press('F1')
        
    if pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90, region=REGION_BUF_BAR) != None:
        print('entrou eenenenene')
        counter = 0
        while counter < 5:
            if event_th.is_set():
                return
            print('comendo!')
            pg.press('u')
            counter += 1
"""            
def check_equip():
    print('checando equips!')
    if pg.locateOnScreen('imgs/amulet_slot.png', confidence=0.90, region=REGION_AMULET) != None:
        if event_th.is_set():
            return
        print('colocando amuleto')
        pg.press('F9')
        pg.sleep(0.2)
    if pg.locateOnScreen('imgs/ring_slot.png', confidence=0.90, region=REGION_RING) != None:
        if event_th.is_set():
            return
        print('colocando ring')
        pg.press('7')
        pg.sleep(0.2)
"""

def run():
    print('inicio')
    while True:
        if event_th.is_set():
            return
        check_status('life')
        pg.sleep(0.2)
        if event_th.is_set():
            return
        check_status('mana')
        pg.sleep(0.2)
        if event_th.is_set():
            return
        #check_equip()


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