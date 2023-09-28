import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import os


FOLDER_NAME = 'lol'


def create_folder():
    if not os.path.isdir(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)

class Rec:
    def __init__(self):
        create_folder()
        self.count = 1

    def photo(self):
        
        pg.sleep(0.3)
        
        photo = pg.screenshot(region=( 1860, 252, 19, 1))
        photo.save(f'{FOLDER_NAME}/flag_up_down_{self.count}.png')
        self.count = self.count + 1
    
    def key_code(self, key):
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.insert:
            self.photo()
        print('key', key)
    
    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()
            

self = Rec()
self.start()