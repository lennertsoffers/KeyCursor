from model.KeyManager import KeyManager
from model.State import State
from model.SystemTrayIcon import SystemTrayIcon
from core.Config import Config
from util.process_util import kill_other_key_cursor_processes


def main():
    state = State()
    config = Config()
    system_tray_icon = SystemTrayIcon(state)
    KeyManager(state, config, system_tray_icon)

    # Must be last call because it is blocking
    system_tray_icon.show()


if __name__ == "__main__":
    kill_other_key_cursor_processes()
    main()
