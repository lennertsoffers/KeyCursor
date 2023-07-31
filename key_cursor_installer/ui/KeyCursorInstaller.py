from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWizard

from Global import Global
from ui.PageFinish import PageFinish
from ui.PageFolderSelection import PageFolderSelection
from ui.PageProgress import PageProgress
from ui.PageWelcome import PageWelcome


class KeyCursorInstaller(QWizard):
    def __init__(self):
        super().__init__()

        self._install_directory = Global.PLATFORM_UTILS.get_default_installation_location() + "/KeyCursor"

        self._page_welcome = PageWelcome(self)
        self._page_folder_selection = PageFolderSelection(self)
        self._page_progress = PageProgress(self)
        self._page_finish = PageFinish(self)

        self._init_layout()

    def remove_buttons(self):
        self.setButtonLayout([])

    def get_install_directory(self):
        return self._install_directory

    def set_install_directory(self, path: str):
        self._install_directory = path

    def _init_layout(self):
        self.setWindowIcon(QIcon(":assets/icon.png"))
        self.setWindowTitle("KeyCursor installer")
        self.setWizardStyle(QWizard.ModernStyle)
        self.setFixedSize(440, 300)

        logo = QPixmap(":assets/icon.png").scaled(35, 35, transformMode=Qt.SmoothTransformation)
        self.setPixmap(QWizard.LogoPixmap, logo)

        self.addPage(self._page_welcome)
        self.addPage(self._page_folder_selection)
        self.addPage(self._page_progress)
        self.addPage(self._page_finish)
