from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kbd = Controller()

is_t_pressed = False
is_f_pressed = False
is_h_pressed = False

def on_press(key):
    global is_t_pressed, is_f_pressed, is_h_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 't' and not is_t_pressed:
                is_t_pressed = True
                kbd.press(Key.up)
                kbd.press('w')
                kbd.press('i')
            
            elif key.char == 'f' and not is_f_pressed:
                is_f_pressed = True
                kbd.press(Key.left)
                kbd.press('a')
                kbd.press('j')
            
            elif key.char == 'h' and not is_h_pressed:
                is_h_pressed = True
                kbd.press(Key.right)
                kbd.press('d')
                kbd.press('l')

    except AttributeError:
        pass

def on_release(key):
    global is_t_pressed, is_f_pressed, is_h_pressed
    try:
        if hasattr(key, 'char'):
            if key.char == 't' and is_t_pressed:
                is_t_pressed = False
                kbd.release(Key.up)
                kbd.release('w')
                kbd.release('i')
            
            elif key.char == 'f' and is_f_pressed:
                is_f_pressed = False
                kbd.release(Key.left)
                kbd.release('a')
                kbd.release('j')
            
            elif key.char == 'h' and is_h_pressed:
                is_h_pressed = False
                kbd.release(Key.right)
                kbd.release('d')
                kbd.release('l')

    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Программа запущена. Используйте клавиши T, F, H для эмуляции.")
    listener.join()