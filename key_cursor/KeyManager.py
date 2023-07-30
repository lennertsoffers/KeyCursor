import keyboard


class KeyManager:
    def __init__(self, state, config):
        self._state = state
        self._config = config
        self._register_callbacks()

    def press_space(self, _):
        self._state.set_space_down()
        self._state.set_moved(False)

    def release_space(self, _):
        self._state.set_space_down(False)

        if not self._state.is_moved():
            keyboard.send("space")

    def press_key(self, event):
        pressed_key = event.name

        if self._state.is_space_down():
            mapped_key = self._config.get_mapping().get(pressed_key)

            if mapped_key is not None:
                keyboard.send(mapped_key)
                self._state.set_moved()
                return

        keyboard.send(pressed_key)

    def _register_callbacks(self):
        keyboard.on_press_key("space", self.press_space, True)
        keyboard.on_release_key("space", self.release_space, True)

        for k in self._config.get_mapping().keys():
            keyboard.on_press_key(k, self.press_key, True)

        print("Registration done!")
