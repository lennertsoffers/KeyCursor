import platform
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from core.Config import Config
from autostart.AutoStartLinux import AutoStartLinux
from autostart.AutoStartMac import AutoStartMac
from autostart.AutoStartWindows import AutoStartWindows
from key_cursor_config.ui.KeyCursorConfig import KeyCursorConfig
from model.StyleLoader import StyleLoader
from util.process_util import kill_other_key_cursor_config_processes
# noinspection PyUnresolvedReferences
import resources.resources


def main():
    config = Config()

    style_loader = StyleLoader(":/style/variables.qss")

    system = platform.system()
    if system == "Windows":
        autostart = AutoStartWindows()
    elif system == "Darwin":
        autostart = AutoStartMac()
    elif system == "Linux":
        autostart = AutoStartLinux()
    else:
        raise Exception("Unsupported operating system: {}".format(system))

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)

    window = KeyCursorConfig(config, autostart, style_loader)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    kill_other_key_cursor_config_processes()
    main()
