from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QWizard


class PageWelcome(QWizardPage):
    def __init__(self, installer):
        super().__init__()

        self._installer = installer

        self._init_layout()

    def _init_layout(self):
        self.setTitle("Welcome to the KeyCursor installation wizard")
        watermark = QPixmap(":/assets/watermark.png").scaled(150, 255, transformMode=Qt.SmoothTransformation)
        self.setPixmap(QWizard.WatermarkPixmap, watermark)

        body_layout = QVBoxLayout()
        label_1 = QLabel("This will install KeyCursor v1.0.0 on your computer.")
        label_1.setWordWrap(True)
        label_2 = QLabel("You will need an internet connection to complete the installation.")
        label_2.setWordWrap(True)
        label_3 = QLabel("Click Next to continue or cancel to exit the setup.")
        label_3.setWordWrap(True)
        body_layout.addWidget(label_1)
        body_layout.addWidget(label_2)
        body_layout.addWidget(label_3)

        self.setLayout(body_layout)
