import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import threading

REGION_BATTLE = (1854, 238, 164, 46)
REGION_SCREEN = (768, 102, 957, 702)
REGION_LOOT = (1165, 370, 167, 167)
REGION_MAP = (2389, 26, 116, 116)
REGION_CENTER_MAP = (2442, 77, 9, 9)
REGION_TARGET_LINE = (1859, 250, 22, 3)
REGION_AMULET = (2393, 185, 32, 32)
REGION_RING = (2393, 257, 32, 32)
REGION_BUF_BAR = (2392, 315, 107, 11)
CENTER_FLOR = (1248, 461)
REGION_FLOR_LEVEL = (2530, 71, 25, 70)
FLOR_LEVEL = None
LIFE_STATUS = (218, 79, 79)
FULL_LIFE_STATUS = (218, 79, 79)
MANA_STATUS = (83, 80, 217)

counter_circle = 1
flag_flor_toggle = 'down'
print(counter_circle)


def check_battle():
    return pg.locateOnScreen('imgs/region_battle.png', confidence=0.95, region=REGION_BATTLE)

def check_center_map():
    return pg.locateOnScreen('imgs/map_center.png', region=REGION_MAP)

def check_flag_center():
    if counter_circle == 1:
        return pg.locateOnScreen('imgs/flag_1.png',confidence=0.8 , region=(REGION_CENTER_MAP))
    elif counter_circle == 2:
        return pg.locateOnScreen('imgs/flag_2.png',confidence=0.6 , region=(REGION_CENTER_MAP))
    elif counter_circle == 3:
        return pg.locateOnScreen('imgs/flag_3.png',confidence=0.8 , region=(REGION_CENTER_MAP))
    elif counter_circle == 4:
        return pg.locateOnScreen('imgs/flag_4.png',confidence=0.8 , region=(REGION_CENTER_MAP))
    
    
def flag_huter_toggle():
    if counter_circle == 1:
        return pg.locateOnScreen('imgs/flag_1.png', region=(REGION_MAP))
    elif counter_circle == 2:
        return pg.locateOnScreen('imgs/flag_2.png', region=(REGION_MAP))
    elif counter_circle == 3:
        return pg.locateOnScreen('imgs/flag_3.png', region=(REGION_MAP))
    elif counter_circle == 4:
        return pg.locateOnScreen('imgs/flag_4.png', region=(REGION_MAP))


def check_flag_flor_center():
    if flag_flor_toggle == 'down':
        return pg.locateOnScreen('imgs/flaggg_down.png',confidence=0.8 , region=(REGION_CENTER_MAP))
    elif flag_flor_toggle == 'up':
        return pg.locateOnScreen('imgs/flaggg_up.png',confidence=0.8 , region=(REGION_CENTER_MAP))
    
def flag_flor_up_down():
    if flag_flor_toggle == 'down':
        return pg.locateOnScreen('imgs/flaggg_down.png', region=(REGION_MAP))
    elif flag_flor_toggle == 'up':
        return pg.locateOnScreen('imgs/flaggg_up.png', region=(REGION_MAP))  

def check_flag_flor_toggle_center():
    return pg.locateOnScreen('imgs/flaggg_toggle.png',confidence=0.8 , region=(REGION_CENTER_MAP))

def flag_flor_toggle_toggle():
    return pg.locateOnScreen('imgs/flaggg_toggle.png', region=(REGION_MAP))

def check_flor_level():
    if pg.locateOnScreen('imgs_flor/flag_up_down_8.png', region=(REGION_FLOR_LEVEL)) != None:
        return '0'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_9.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd1'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_10.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd2'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_11.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd3'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_12.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd4'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_13.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd5'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_14.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd6'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_15.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd7'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_16.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'd8'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_7.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u1'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_6.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u2'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_5.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u3'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_4.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u4'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_3.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u5'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_2.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u6'
    elif pg.locateOnScreen('imgs_flor/flag_up_down_1.png', region=(REGION_FLOR_LEVEL)) != None:     
        return 'u7'

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
    if pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90, region=REGION_BUF_BAR) != None:
        counter = 0
        while counter < 5:
            if event_th.is_set():
                return
            print('comendo!')
            pg.press('u')
            counter += 1
        pg.sleep(0.2)    
        

def flor_level_att():
    global FLOR_LEVEL
    FLOR_LEVEL = check_flor_level()

def circle_rotation():
    global counter_circle  # Indica que estamos usando a variável global
    if counter_circle == 1:
        counter_circle = 2
    elif counter_circle == 2:
        counter_circle = 3
    elif counter_circle == 3:
        counter_circle = 4
    elif counter_circle == 4:
        counter_circle = 1 
    
    
def combat():
    while pg.locateOnScreen('imgs/target.png',confidence=0.89 , region=REGION_TARGET_LINE) != None:
        if event_th.is_set():
            return
        print('atacando o alvo')
        check_status()
        pg.sleep(0.2)
        

def check_status():
    
    print('checando status!')
    if event_th.is_set():
        return
    if pg.pixel(2497, 147) != FULL_LIFE_STATUS:
        if pg.pixel(2446, 147) != LIFE_STATUS:
            pg.press('3')
        elif pg.pixel(2474, 147) != LIFE_STATUS:
            pg.press('2')
        elif pg.pixel(2485, 147) != LIFE_STATUS:
            pg.press('1')
        pg.sleep(0.3)
    if event_th.is_set():
        return
    if pg.pixel(2497, 160) != MANA_STATUS:
        if pg.pixel(2446, 160) != MANA_STATUS:
            pg.press('f')
        pg.sleep(0.3)
    #if pg.locateOnScreen('imgs/buf_speed.png', confidence=0.90, region=REGION_BUF_BAR) == None:
        #if event_th.is_set():
            #return
        #print('buf speed!')
        #pg.press('4')
        #pg.sleep(0.4)
 
def get_loot():
    counter = 0
    while counter < 2:
        if event_th.is_set():
            return
        pg.click(button="middle")
        pg.sleep(0.05)
        counter += 1
    
 
def get_loot_on_screen(): 
    counter = 0
    while counter < 4:
        print('procurando loot')  
        loot = pg.locateOnScreen('imgs/loot_monster.png', confidence=0.6)
        if loot != None:
            print('achei loot') 
            x, y = pg.center(loot)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(4)
            pg.click(button="middle")
            pg.sleep(0.3)
        counter += 1
            
   
def kill_Monster():
    while check_battle() == None:
        if event_th.is_set():
            return
        print('novo alvo!')
        pg.press('space')
        combat()
        if event_th.is_set():
            return
        print('Monstro morto!')
        get_loot()
        if event_th.is_set():
            return
        print('Procurando outro monstro!')
        
       
def hunt_rotation():
    global FLOR_LEVEL
    global flag_flor_toggle
    if flag_huter_toggle() != None:
        if counter_circle == 1:
            circle_toggle = 1
            while circle_toggle == 1:
                if event_th.is_set():
                    return
                if check_flag_center() == None:
                    kill_Monster()
                    #get_loot_on_screen()
                    flag_hunter = flag_huter_toggle()
                    x, y = pg.center(flag_hunter)
                    pg.moveTo(x, y)
                    pg.click()
                    print(flag_huter_toggle())
                    pg.moveTo(2488, 904)
                    check_status()
                    check_equip()
                    kill_Monster()
                    #get_loot_on_screen()
                    pg.sleep(0.5)
                else:
                    circle_toggle = 2
                    circle_rotation()
        elif counter_circle == 2:
            circle_toggle = 1
            while circle_toggle == 1:
                if event_th.is_set():
                    return
                if check_flag_center() == None:
                    kill_Monster()
                    
                    #get_loot_on_screen()
                    flag_hunter = flag_huter_toggle()
                    x, y = pg.center(flag_hunter)
                    pg.moveTo(x, y)
                    pg.click()
                    print(flag_huter_toggle())
                    print(check_flag_center())
                    pg.moveTo(2488, 904)
                    check_status()
                    kill_Monster()
                    #get_loot_on_screen()
                    pg.sleep(0.5)
                else:
                    circle_toggle = 2
                    circle_rotation()
        elif counter_circle == 3:
            circle_toggle = 1
            while circle_toggle == 1:
                if event_th.is_set():
                    return
                if check_flag_center() == None:
                    kill_Monster()
                    #get_loot_on_screen()
                    flag_hunter = flag_huter_toggle()
                    x, y = pg.center(flag_hunter)
                    pg.moveTo(x, y)
                    pg.click()
                    pg.moveTo(2488, 904)
                    check_status()
                    check_equip()
                    kill_Monster()
                    #get_loot_on_screen()
                    pg.sleep(0.5)
                else:
                    circle_toggle = 2
                    circle_rotation()
        elif counter_circle == 4:
            circle_toggle = 1
            while circle_toggle == 1:
                if event_th.is_set():
                    return
                if check_flag_center() == None:
                    kill_Monster()
                    #get_loot_on_screen()
                    flag_hunter = flag_huter_toggle()
                    x, y = pg.center(flag_hunter)
                    pg.moveTo(x, y)
                    pg.click()
                    pg.moveTo(2488, 904)
                    check_status()
                    kill_Monster()
                    #get_loot_on_screen()
                    pg.sleep(0.5)
                else:
                    circle_toggle = 2
                    circle_rotation()
                    
            if flag_flor_up_down() != None:
                if flag_flor_toggle == 'down':
                    circle_flag_toggle = 1
                    while circle_flag_toggle == 1:
                        if event_th.is_set():
                            return
                        if check_flag_flor_center() == None:
                            if FLOR_LEVEL != check_flor_level():
                                FLOR_LEVEL = check_flor_level()
                                pg.sleep(1)
                                run()
                            kill_Monster()
                            #get_loot_on_screen()
                            flor_toggle = flag_flor_up_down()
                            x, y = pg.center(flor_toggle)
                            pg.moveTo(x, y)
                            pg.click()
                            pg.moveTo(2488, 904)
                            check_status()
                            kill_Monster()
                            #get_loot_on_screen()
                            pg.sleep(0.5)
                        else:
                            pg.press('b') 
                            pg.moveTo(CENTER_FLOR)
                            pg.click()
                            circle_flag_toggle = 2
                            pg.sleep(1)
            
                elif flag_flor_toggle == 'up':
                    circle_flag_toggle = 1
                    while circle_flag_toggle == 1:
                        if event_th.is_set():
                            return
                        if check_flag_flor_center() == None:
                            kill_Monster()
                            #get_loot_on_screen()
                            flor_toggle = flag_flor_up_down()
                            x, y = pg.center(flor_toggle)
                            pg.moveTo(x, y)
                            pg.click()
                            pg.moveTo(2488, 904)
                            kill_Monster()
                            #get_loot_on_screen()
                            pg.sleep(0.5)
                        else:
                            pg.sleep(0.7)
                            pg.moveTo(CENTER_FLOR)
                            pg.sleep(0.3)
                            pg.click(button="right")
                            pg.sleep(0.3)
                            pg.press('v') 
                            pg.moveTo(CENTER_FLOR)
                            pg.sleep(0.3)
                            pg.click()
                            flag_flor_toggle = 'down'
                            FLOR_LEVEL = check_flor_level()
                            circle_flag_toggle = 2
                            pg.sleep(1) 
                            
            elif flag_flor_toggle_toggle() != None:
                if flag_flor_toggle == 'down':
                    circle_flag_toggle = 1
                    while circle_flag_toggle == 1:
                        if event_th.is_set():
                            return
                        if check_flag_flor_toggle_center() == None:
                            if FLOR_LEVEL != check_flor_level():
                                FLOR_LEVEL = check_flor_level()
                                flag_flor_toggle = 'up'
                                pg.sleep(1)
                                run()
                            kill_Monster()
                            #get_loot_on_screen()
                            flor_toggle = flag_flor_toggle_toggle()
                            x, y = pg.center(flor_toggle)
                            pg.moveTo(x, y)
                            pg.click()
                            pg.moveTo(2488, 904)
                            check_status()
                            kill_Monster()
                            #get_loot_on_screen()
                            pg.sleep(0.5)
                        else:
                            pg.press('b') 
                            pg.moveTo(CENTER_FLOR)
                            pg.click()
                            flag_flor_toggle = 'up'
                            circle_flag_toggle = 2 
                            pg.sleep(1)  
                            
                elif flag_flor_toggle == 'up':
                    circle_flag_toggle = 1
                    while circle_flag_toggle == 1:
                        if event_th.is_set():
                            return
                        if check_flag_flor_toggle_center() == None:
                            kill_Monster()
    
                            check_status()
                            
                            #get_loot_on_screen()
                            flor_toggle = flag_flor_toggle_toggle()
                            x, y = pg.center(flor_toggle)
                            pg.moveTo(x, y)
                            pg.click()
                            pg.moveTo(2488, 904)
                            kill_Monster()
                            #get_loot_on_screen()
                            pg.sleep(0.5)
                        else:
                            pg.sleep(0.3)
                            pg.moveTo(CENTER_FLOR)
                            pg.sleep(0.6)
                            pg.click(button="right")
                            pg.sleep(0.3)
                            pg.press('v') 
                            pg.moveTo(CENTER_FLOR)
                            pg.sleep(0.3)
                            pg.click()
                            flag_flor_toggle = 'down'
                            FLOR_LEVEL = check_flor_level()
                            circle_flag_toggle = 2
                            pg.sleep(1)  
                            
    else:
        circle_rotation()            

def run():
    print('inicio')
    flor_level_att()
    while True:
        if event_th.is_set():
            return
        hunt_rotation()
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
    
        
        
 
#pg.displayMousePosition()
#print(pg.pixel(2492, 160))
   


