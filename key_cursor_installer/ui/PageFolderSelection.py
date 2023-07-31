from PyQt5.QtWidgets import QWizardPage, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QWizard


class PageFolderSelection(QWizardPage):
    def __init__(self, installer):
        super().__init__()

        self._installer = installer

        self._init_layout()

    def validatePage(self) -> bool:
        self._installer.remove_buttons()
        return True

    def _init_layout(self):
        self.setButtonText(QWizard.NextButton, "Install")
        self.setTitle("Select installation folder")
        self.setSubTitle("Where should KeyCursor be installed?")

        body_layout = QVBoxLayout()
        body_layout.setSpacing(20)

        folder_label = QLabel("Setup will install KeyCursor into the following folder.")
        folder_label.setWordWrap(True)
        folder_warning_label = QLabel("Make sure you have edit rights in this directory.")
        folder_warning_label.setWordWrap(True)
        installation_folder_label = QLabel("To continue, click Next. If you would like to select a different folder, click Browse.")
        installation_folder_label.setWordWrap(True)

        browse_layout = QHBoxLayout()
        self._browse_layout_input = QLineEdit()
        self._browse_layout_input.setText(self._installer.get_install_directory())
        browse_button = QPushButton("Browse...")
        browse_button.clicked.connect(self._on_browse_button_click)
        browse_layout.addWidget(self._browse_layout_input)
        browse_layout.addWidget(browse_button)

        body_layout.addWidget(folder_label)
        body_layout.addWidget(installation_folder_label)
        body_layout.addLayout(browse_layout)

        self.setLayout(body_layout)

    def _on_browse_button_click(self):
        selected_folder = QFileDialog.getExistingDirectory(self, 'Select Folder', '', QFileDialog.ShowDirsOnly)

        if selected_folder:
            folder_path = selected_folder + "/KeyCursor"
            self._browse_layout_input.setText(folder_path)
            self._installer.set_install_directory(folder_path)
