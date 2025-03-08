from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kbd = Controller()

is_up_pressed = False
is_right_pressed = False
is_left_pressed = False

def on_press(key):
    global is_up_pressed, is_right_pressed, is_left_pressed
    try:
        if key == Key.up and not is_up_pressed:
            is_up_pressed = True
            kbd.press('w')
            kbd.press('t')
            kbd.press('i')
        
        elif key == Key.right and not is_right_pressed:
            is_right_pressed = True
            kbd.press('d')
            kbd.press('h')
            kbd.press('l')
        
        elif key == Key.left and not is_left_pressed:
            is_left_pressed = True
            kbd.press('a')
            kbd.press('f')
            kbd.press('j')

    except AttributeError:
        pass

def on_release(key):
    global is_up_pressed, is_right_pressed, is_left_pressed
    try:
        if key == Key.up and is_up_pressed:
            is_up_pressed = False
            kbd.release('w')
            kbd.release('t')
            kbd.release('i')
        
        elif key == Key.right and is_right_pressed:
            is_right_pressed = False
            kbd.release('d')
            kbd.release('h')
            kbd.release('l')
        
        elif key == Key.left and is_left_pressed:
            is_left_pressed = False
            kbd.release('a')
            kbd.release('f')
            kbd.release('j')
        
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("The program is running. Use the arrows to emulate the keys.")
    listener.join()