import keyboard
from pynput.keyboard import Controller, Key

from Config import Config
from Keys import Keys
from model.State import State
from model.SystemTrayIcon import SystemTrayIcon


class KeyManager:
    def __init__(self, state: State, config: Config, system_tray_icon: SystemTrayIcon):
        self._state = state
        self._config = config
        self._system_tray_icon = system_tray_icon
        self._register_callbacks()
        self._controller = Controller()
        self._print_space = True
        self._modifiers = {
            "shift": False,
            "right shift": False
        }

    def _press_activation_key(self, _event):
        if self._state.is_suspended():
            keyboard.send(self._config.get_activation_key())
        else:
            self._state.set_activation_key_down()
            self._state.set_moved(False)

    def _release_activation_key(self, _event):
        self._state.set_activation_key_down(False)

        if not self._state.is_moved() and not self._state.is_suspended() and self._print_space:
            keyboard.send(self._config.get_activation_key())

        self._print_space = True

    def _press_key(self, event):
        pressed_key = event.name
        resulting_key = pressed_key

        if self._state.is_activation_key_down() and not self._state.is_suspended():
            mapped_key = self._config.get_mapping().get(pressed_key)

            if mapped_key is not None:
                resulting_key = mapped_key
                self._state.set_moved()
            else:
                self._controller.release(Key.space)
                self._print_space = False

        if resulting_key in Keys.characters:
            press_shift_l = False
            press_shift_r = False

            if self._is_keybind_active():
                resulting_key = resulting_key.lower()
            else:
                if self._modifiers.get("shift") is True:
                    print(self._modifiers)
                    self._controller.release(Key.shift_l)
                    press_shift_l = True
                if self._modifiers.get("right shift") is True:
                    self._controller.release(Key.shift_r)
                    press_shift_r = True

            self._controller.type(resulting_key)

            if press_shift_l is True:
                self._controller.press(Key.shift_l)
            if press_shift_r is True:
                self._controller.press(Key.shift_r)

            if self._state.is_moved() and self._state.is_activation_key_down():
                self._controller.press(Keys.keyboard_to_pynput.get(self._config.get_activation_key()))
                self._print_space = False
        else:
            keyboard.send(resulting_key)

    def _press_suspension_key(self, _event):
        self._state.toggle_suspension()
        self._system_tray_icon.update()

    def _press_modifier_key(self, event):
        self._modifiers[event.name] = True

    def _release_modifier_key(self, event):
        self._modifiers[event.name] = False

    def _register_callbacks(self):
        activation_key = self._config.get_activation_key()
        if activation_key is not None:
            keyboard.on_press_key(self._config.get_activation_key(), self._press_activation_key, True)
            keyboard.on_release_key(self._config.get_activation_key(), self._release_activation_key, True)

        suspension_key = self._config.get_suspension_key()
        if suspension_key is not None:
            keyboard.on_press_key(suspension_key, self._press_suspension_key, False)

        for key in Keys.modifier_keys:
            keyboard.on_press_key(key, self._press_modifier_key, False)
            keyboard.on_release_key(key, self._release_modifier_key, False)

        for key in self._config.get_mapping().keys():
            keyboard.on_press_key(key, self._press_key, True)

    def _is_keybind_active(self):
        return any({key: value for key, value in self._modifiers.items() if key not in ["shift", "right shift"]}.values())
