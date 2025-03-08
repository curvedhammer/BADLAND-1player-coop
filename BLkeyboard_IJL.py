from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kbd = Controller()

is_i_pressed = False
is_j_pressed = False
is_l_pressed = False

def on_press(key):
    global is_i_pressed, is_j_pressed, is_l_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 'i' and not is_i_pressed:
                is_i_pressed = True
                kbd.press(Key.up)
                kbd.press('w')
                kbd.press('t')
            
            elif key.char == 'j' and not is_j_pressed:
                is_j_pressed = True
                kbd.press(Key.left)
                kbd.press('a')
                kbd.press('f')
            
            elif key.char == 'l' and not is_l_pressed:
                is_l_pressed = True
                kbd.press(Key.right)
                kbd.press('d')
                kbd.press('h')

    except AttributeError:
        pass

def on_release(key):
    global is_i_pressed, is_j_pressed, is_l_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 'i' and is_i_pressed:
                is_i_pressed = False
                kbd.release(Key.up)
                kbd.release('w')
                kbd.release('t')
            
            elif key.char == 'j' and is_j_pressed:
                is_j_pressed = False
                kbd.release(Key.left)
                kbd.release('a')
                kbd.release('f')
            
            elif key.char == 'l' and is_l_pressed:
                is_l_pressed = False
                kbd.release(Key.right)
                kbd.release('d')
                kbd.release('h')

    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Программа запущена. Используйте клавиши I, J, L для эмуляции.")
    listener.join()