import keyboard
import pyautogui
from pynput.keyboard import Listener, Key, Controller

state = {}
controller = Controller()


def on_press(pressed_key):
    key = str(pressed_key.char) if hasattr(pressed_key, 'char') else str(pressed_key).replace("Key.", "")

    state[key] = True

    print(state)

    if state.get("space") is True and state.get("a") is True:
        controller.release(Key.shift_r)
        controller.type("7")


def on_release(pressed_key):
    key = str(pressed_key.char) if hasattr(pressed_key, 'char') else str(pressed_key).replace("Key.", "")
    state[key] = False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
