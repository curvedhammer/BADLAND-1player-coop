from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kbd = Controller()

is_w_pressed = False
is_a_pressed = False
is_d_pressed = False

def on_press(key):
    global is_w_pressed, is_a_pressed, is_d_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 'w' and not is_w_pressed:
                is_w_pressed = True
                kbd.press(Key.up)
                kbd.press('t')
                kbd.press('i')
            
            elif key.char == 'a' and not is_a_pressed:
                is_a_pressed = True
                kbd.press(Key.left)
                kbd.press('f')
                kbd.press('j')
            
            elif key.char == 'd' and not is_d_pressed:
                is_d_pressed = True
                kbd.press(Key.right)
                kbd.press('h')
                kbd.press('l')

    except AttributeError:
        pass

def on_release(key):
    global is_w_pressed, is_a_pressed, is_d_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 'w' and is_w_pressed:
                is_w_pressed = False
                kbd.release(Key.up)
                kbd.release('t')
                kbd.release('i')
            
            elif key.char == 'a' and is_a_pressed:
                is_a_pressed = False
                kbd.release(Key.left)
                kbd.release('f')
                kbd.release('j')
            
            elif key.char == 'd' and is_d_pressed:
                is_d_pressed = False
                kbd.release(Key.right)
                kbd.release('h')
                kbd.release('l')

    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("The program is running. Use the arrows to emulate the keys.")
    listener.join()