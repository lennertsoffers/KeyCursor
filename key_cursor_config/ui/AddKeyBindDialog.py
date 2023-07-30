from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QPushButton

from key_cursor_config.model.Key import Key
from key_cursor_config.model.KeyBind import KeyBind
from key_cursor_config.ui.global_style import *


class AddKeyBindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add new key binding")
        self.setFixedSize(300, 270)
        self.setWindowIcon(QIcon(icon_path))

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        dropdown_layout_to_press = QVBoxLayout()
        dropdown_layout_to_press.setAlignment(Qt.AlignTop)
        dropdown_layout_to_press.setSpacing(10)

        dropdown_layout_to_generate = QVBoxLayout()
        dropdown_layout_to_generate.setAlignment(Qt.AlignTop)
        dropdown_layout_to_generate.setSpacing(10)

        to_press_label = QLabel("Key to press:")
        to_press_label.setFont(font_poppins)
        to_press_label.setStyleSheet(label_style)
        self._to_press_dropdown = QComboBox()
        self._to_press_dropdown.addItems(e.value for e in Key)
        self._to_press_dropdown.setFont(font_poppins)
        self._to_press_dropdown.setStyleSheet(dropdown_style)
        dropdown_layout_to_press.addWidget(to_press_label)
        dropdown_layout_to_press.addWidget(self._to_press_dropdown)

        to_generate_label = QLabel("Key to generate:")
        to_generate_label.setFont(font_poppins)
        to_generate_label.setStyleSheet(label_style)
        self._to_generate_dropdown = QComboBox()
        self._to_generate_dropdown.addItems(e.value for e in Key)
        self._to_generate_dropdown.setFont(font_poppins)
        self._to_generate_dropdown.setStyleSheet(dropdown_style)
        dropdown_layout_to_generate.addWidget(to_generate_label)
        dropdown_layout_to_generate.addWidget(self._to_generate_dropdown)

        button_layout = QHBoxLayout()
        confirm_button = QPushButton("Confirm", self)
        confirm_button.clicked.connect(self.accept)
        confirm_button.setStyleSheet(button_confirm_style)
        confirm_button.setFont(font_poppins)
        confirm_button.setCursor(Qt.PointingHandCursor)
        cancel_button = QPushButton("Cancel", self)
        cancel_button.clicked.connect(self.reject)
        cancel_button.setStyleSheet(button_cancel_style)
        cancel_button.setFont(font_poppins)
        cancel_button.setCursor(Qt.PointingHandCursor)
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(dropdown_layout_to_press)
        layout.addLayout(dropdown_layout_to_generate)
        layout.addLayout(button_layout)

    def get_key_bind(self) -> KeyBind:
        return KeyBind(self._to_press_dropdown.currentText(), self._to_generate_dropdown.currentText())
