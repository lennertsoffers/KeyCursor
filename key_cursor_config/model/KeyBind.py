class KeyBind:
    def __init__(self, key_to_press, key_to_generate):
        self._key_to_press = key_to_press
        self._key_to_generate = key_to_generate

    def __str__(self):
        return self._key_to_press + " -> " + self._key_to_generate

    def to_press(self):
        return self._key_to_press

    def to_generate(self):
        return self._key_to_generate
