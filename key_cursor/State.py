class State:
    def __init__(self):
        self._space_down = False
        self._moved = False

    def is_space_down(self):
        return self._space_down

    def is_moved(self):
        return self._moved

    def set_space_down(self, down=True):
        self._space_down = down

    def set_moved(self, moved=True):
        self._moved = moved
