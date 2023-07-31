import keyboard

from Config import Config
from State import State
from SystemTrayIcon import SystemTrayIcon


class KeyManager:
    def __init__(self, state: State, config: Config, system_tray_icon: SystemTrayIcon):
        self._state = state
        self._config = config
        self._system_tray_icon = system_tray_icon
        self._register_callbacks()

    def _press_activation_key(self, _event):
        if self._state.is_suspended():
            keyboard.send(self._config.get_activation_key())
        else:
            self._state.set_activation_key_down()
            self._state.set_moved(False)

    def _release_activation_key(self, _event):
        self._state.set_activation_key_down(False)

        if not self._state.is_moved() and not self._state.is_suspended():
            keyboard.send(self._config.get_activation_key())

    def _press_key(self, event):
        pressed_key = event.name

        if self._state.is_activation_key_down() and not self._state.is_suspended():
            mapped_key = self._config.get_mapping().get(pressed_key)

            if mapped_key is not None:
                keyboard.send(mapped_key)
                self._state.set_moved()
                return

        keyboard.send(pressed_key)

    def _press_suspension_key(self, _event):
        self._state.toggle_suspension()
        self._system_tray_icon.update()

    def _register_callbacks(self):
        activation_key = self._config.get_activation_key()
        if activation_key is not None:
            keyboard.on_press_key(self._config.get_activation_key(), self._press_activation_key, True)
            keyboard.on_release_key(self._config.get_activation_key(), self._release_activation_key, True)

        suspension_key = self._config.get_suspension_key()
        if suspension_key is not None:
            keyboard.on_press_key(suspension_key, self._press_suspension_key, False)

        for k in self._config.get_mapping().keys():
            keyboard.on_press_key(k, self._press_key, True)
