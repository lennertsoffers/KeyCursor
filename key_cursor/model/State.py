class State:
    def __init__(self):
        self._activation_key_down = False
        self._moved = False
        self._suspended = False

    def is_activation_key_down(self):
        return self._activation_key_down

    def is_moved(self):
        return self._moved

    def is_suspended(self):
        return self._suspended

    def set_activation_key_down(self, down=True):
        self._activation_key_down = down

    def set_moved(self, moved=True):
        self._moved = moved

    def toggle_suspension(self):
        self._suspended = not self._suspended
