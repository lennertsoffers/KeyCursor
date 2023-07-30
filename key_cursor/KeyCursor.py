from KeyManager import KeyManager
from State import State
from core.Config import Config
from key_cursor.system_tray import show_system_tray_icon


def setup():
    state = State()
    config = Config()
    KeyManager(state, config)


def main():
    # TODO - Don't start twice when executing
    setup()
    show_system_tray_icon()


if __name__ == "__main__":
    main()
