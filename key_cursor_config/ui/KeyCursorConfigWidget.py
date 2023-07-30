import subprocess
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QCheckBox, QDialog
from PyQt5.QtCore import Qt
import psutil
from PyQt5 import QtGui

from core.Config import Config

from core.autostart.AutoStart import AutoStart
from key_cursor_config.model.KeyBind import KeyBind
from key_cursor_config.ui.AddKeyBindDialog import AddKeyBindDialog
from key_cursor_config.ui.global_style import *


def get_daemon_processes():
    processes = []
    for process in psutil.process_iter():
        if "KeyCursor" in process.name() and "KeyCursorConfig" not in process.name():
            processes.append(process)

    return processes


class KeyCursorConfigWidget(QWidget):
    def __init__(self, config: Config, autostart: AutoStart):
        super().__init__()
        self.key_bind_checkboxes = []
        self.key_binds = []

        self._config = config
        self._autostart = autostart

        self.checkbox_layout = None
        self.setWindowTitle("KeyCursorConfig")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(340, 400)
        self.setStyleSheet(f"background-color: {colour_black};")

        self._init_layout()
        self._load()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        daemons = get_daemon_processes()
        if len(daemons) > 0:
            for daemon in daemons:
                daemon.kill()
            subprocess.Popen("KeyCursor")

    def _init_layout(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignTop)

        # Enable button
        self._enable_button = QPushButton(self)
        self._enable_button.setFixedHeight(40)
        self._enable_button.setFont(font_poppins)
        self._enable_button.setCursor(Qt.PointingHandCursor)
        self._enable_button.clicked.connect(self._on_enable_button_click)
        self._update_enable_button()
        main_layout.addWidget(self._enable_button)

        # Checkboxes
        checkbox_layout = QVBoxLayout()
        checkbox_layout.setSpacing(10)
        checkbox_run_at_startup = QCheckBox("Run at startup", self)
        checkbox_run_at_startup.setStyleSheet(checkbox_style)
        checkbox_run_at_startup.setFont(font_poppins)
        checkbox_run_at_startup.setChecked(self._config.is_run_at_startup())
        checkbox_run_at_startup.stateChanged.connect(self._on_enable_on_startup_checkbox_state_change)
        checkbox_layout.addWidget(checkbox_run_at_startup)
        main_layout.addLayout(checkbox_layout)

        # Key bindings
        key_binds_scroll_area = QScrollArea(self)
        key_binds_scroll_area.setObjectName("key_binds_scroll_area")
        key_binds_scroll_area.setStyleSheet(
            f"QScrollArea#key_binds_scroll_area {{ border-radius: {border_radius}; border: 2px solid {colour_white}; }}")
        key_binds_scroll_area.verticalScrollBar().setStyleSheet("QScrollBar { width: 0px; }")
        key_binds_scroll_area.setWidgetResizable(True)
        key_binds_scroll_area.setFixedHeight(200)
        key_binds_widget = QWidget(key_binds_scroll_area)
        key_binds_widget.setStyleSheet("background-color: transparent;")
        key_binds_layout = QVBoxLayout(key_binds_widget)
        key_binds_layout.setAlignment(Qt.AlignTop)
        key_binds_layout.setContentsMargins(10, 10, 10, 10)
        key_binds_widget.setLayout(key_binds_layout)
        key_binds_scroll_area.setWidget(key_binds_widget)
        main_layout.addWidget(key_binds_scroll_area)

        # Add and remove buttons
        buttons_layout = QHBoxLayout()

        add_button = QPushButton("Add", self)
        add_button.setFixedHeight(40)
        add_button.setStyleSheet(button_confirm_style)
        add_button.setFont(font_poppins)
        add_button.setCursor(Qt.PointingHandCursor)
        add_button.clicked.connect(self._on_add_button_click)

        remove_button = QPushButton("Remove", self)
        remove_button.setFixedHeight(40)
        remove_button.setStyleSheet(button_cancel_style)
        remove_button.setFont(font_poppins)
        remove_button.setCursor(Qt.PointingHandCursor)
        remove_button.clicked.connect(self._on_remove_button_click)

        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(remove_button)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.checkbox_layout = key_binds_layout

    def _load(self):
        for key, value in self._config.get_mapping().items():
            self.key_binds.append(KeyBind(key, value))
        self._update_scroll_area()

        if self._config.is_run_at_startup():
            self._autostart.register_autostart()
        else:
            self._autostart.disable_autostart()

    def _on_enable_button_click(self):
        daemons = get_daemon_processes()
        if len(daemons) == 0:
            subprocess.Popen("KeyCursor")
        else:
            for daemon in daemons:
                daemon.kill()

        time.sleep(0.25)
        self._update_enable_button()

    def _on_add_button_click(self):
        dialog = AddKeyBindDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            new_key_bind = dialog.get_key_bind()

            if not any(key_bind.to_press() == new_key_bind.to_press() for key_bind in self.key_binds):
                self.key_binds.append(new_key_bind)
                self._update_scroll_area()
                self._config.add_mapping(new_key_bind.to_press(), new_key_bind.to_generate())

    def _on_remove_button_click(self):
        selected_indices = [idx for idx, checkbox in enumerate(self.key_bind_checkboxes) if checkbox.isChecked()]

        for index in selected_indices:
            self._config.remove_mapping(self.key_binds[index].to_press())

        self.key_binds = [self.key_binds[i] for i in range(len(self.key_binds)) if i not in selected_indices]
        self._update_scroll_area()

    def _on_enable_on_startup_checkbox_state_change(self, checked):
        if checked:
            self._autostart.register_autostart()
            self._config.set_run_at_startup(True)
        else:
            self._autostart.disable_autostart()
            self._config.set_run_at_startup(False)

    def _update_enable_button(self):
        if len(get_daemon_processes()) == 0:
            self._enable_button.setText("Enable")
            self._enable_button.setStyleSheet(button_confirm_style)
        else:
            self._enable_button.setText("Disable")
            self._enable_button.setStyleSheet(button_cancel_style)

    def _update_scroll_area(self):
        # Clear old checkboxes
        for checkbox in self.key_bind_checkboxes:
            self.checkbox_layout.removeWidget(checkbox)
            checkbox.setParent(None)
        self.key_bind_checkboxes = []

        # Add new checkboxes
        for key_bind in self.key_binds:
            checkbox = QCheckBox(key_bind.__str__(), self)
            checkbox.setStyleSheet(checkbox_style)
            checkbox.setFont(font_poppins)
            self.checkbox_layout.addWidget(checkbox)
            self.key_bind_checkboxes.append(checkbox)
