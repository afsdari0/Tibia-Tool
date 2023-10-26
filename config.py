import pyautogui as pg
import keyboard


#pip install pynput
#pip install pillow opencv-python
#pip install pyautogui
#pip install keyboard




print('region_battle',pg.locateOnScreen('imgs/region_battle.png', confidence=0.9))
print('map',pg.locateOnScreen('imgs/map.png', confidence=0.78))
print('region_flor_level',pg.locateOnScreen('imgs_flor/flag_up_down_8.png'))
print('region_target',pg.locateOnScreen('imgs/target.png', confidence=0.89))
print('region_center_map',pg.locateOnScreen('imgs/flag_1.png', confidence=0.89))
print('region_amulet',pg.locateOnScreen('imgs/amulet_slot.png', confidence=0.90))
print('Region_ring',pg.locateOnScreen('imgs/ring_slot.png', confidence=0.90))
print('Region_speedh',pg.locateOnScreen('imgs/buf_speed.png', confidence=0.90))
print('Region_amulet',pg.locateOnScreen('imgs/buf_hungry.png', confidence=0.90))
print('Region_speedh',pg.locateOnScreen('imgs/buff_bar.png', confidence=0.90))
keyboard.wait('h')
print(pg.displayMousePosition())


