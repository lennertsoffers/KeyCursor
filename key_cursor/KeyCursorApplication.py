from KeyManager import KeyManager
from State import State
from SystemTrayIcon import SystemTrayIcon
from core.Config import Config
from util.process_util import is_key_cursor_running


def main():
    state = State()
    config = Config()
    system_tray_icon = SystemTrayIcon(state)
    KeyManager(state, config, system_tray_icon)

    # Must be last call because it is blocking
    system_tray_icon.show()


if __name__ == "__main__":
    if not is_key_cursor_running():
        main()
