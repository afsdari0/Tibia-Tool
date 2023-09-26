import pyautogui as pg
import keyboard


#pip install pynput
#pip install pillow opencv-python
#pip install pyautogui




print(pg.locateOnScreen('imgs/region_battle.png', confidence=0.9))
print(pg.locateOnScreen('imgs/map.png', confidence=0.78))

print(pg.pixel(2474, 147))
keyboard.wait('h')
print(pg.displayMousePosition())


