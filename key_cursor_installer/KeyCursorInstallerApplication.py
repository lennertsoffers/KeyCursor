import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from ui.KeyCursorInstaller import KeyCursorInstaller
# noinspection PyUnresolvedReferences
import resources.resources


def main():
    # - Welcome page
    # - Choose installation folder
    # - Pull zip from cloud
    # - Extract files
    # - Move files to installation folder
    # - Display done message (and option to open application on 'finish')

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DisableWindowContextHelpButton)

    wizard = KeyCursorInstaller()
    wizard.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
