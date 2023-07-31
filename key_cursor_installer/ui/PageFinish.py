import os
import subprocess

from PyQt5.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QCheckBox


class PageFinish(QWizardPage):
    def __init__(self, installer):
        super().__init__()

        self._installer = installer

        self._launch_checkbox = None

        self._init_layout()

    def validatePage(self) -> bool:
        if self._launch_checkbox.isChecked():
            os.chdir(self._installer.get_install_directory())
            subprocess.Popen("KeyCursorConfig")
        return True

    def _init_layout(self):
        self.setTitle("Setup successful")
        self.setSubTitle("Thank you installing KeyCursor")

        body_layout = QVBoxLayout()
        body_layout.setSpacing(20)

        label_1 = QLabel("Note that you'll need to enable KeyCursor before it will be active.")
        label_1.setWordWrap(True)
        label_2 = QLabel("Enabling KeyCursor and many more changes can be made with the configuration application")
        label_2.setWordWrap(True)
        body_layout.addWidget(label_1)
        body_layout.addWidget(label_2)

        self._launch_checkbox = QCheckBox("Launch config")
        self._launch_checkbox.setChecked(True)
        body_layout.addWidget(self._launch_checkbox)

        self.setLayout(body_layout)
