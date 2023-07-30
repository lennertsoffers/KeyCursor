import platform
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from core.Config import Config
from core.autostart.AutoStartLinux import AutoStartLinux
from core.autostart.AutoStartMac import AutoStartMac
from core.autostart.AutoStartWindows import AutoStartWindows
from key_cursor_config.ui.KeyCursorConfigWidget import KeyCursorConfigWidget

if __name__ == "__main__":
    config = Config()

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

    window = KeyCursorConfigWidget(config, autostart)
    window.show()

    sys.exit(app.exec_())
