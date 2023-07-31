from PyQt5.QtWidgets import QWizardPage, QProgressBar, QVBoxLayout, QLabel, QWizard

from model.InstallerThread import InstallerThread


class PageProgress(QWizardPage):
    def __init__(self, installer):
        super().__init__()

        self._installer_thread = None
        self._installer_steps = 0
        self._installer = installer

        self._finished = False

        self._init_layout()

    def initializePage(self) -> None:
        try:
            self._installer_thread = InstallerThread(self._installer.get_install_directory())
            self._installer_steps = self._installer_thread.get_amount_of_steps()
            self._installer_thread.get_progress_signal().connect(self._update_progress)
            self._installer_thread.get_step_signal().connect(self._update_step)
            self._installer_thread.get_finished_signal().connect(self._installer_finished)
            self._installer_thread.start()
        except Exception as e:
            print(e)

    def isComplete(self) -> bool:
        return self._finished

    def _init_layout(self):
        self.setTitle("KeyCursor is now installing")
        self.setSubTitle("Please wait for the installation process to finish")

        body_layout = QVBoxLayout()

        self._progress_bar_label = QLabel()
        body_layout.addWidget(self._progress_bar_label)

        self._progress_bar = QProgressBar()
        body_layout.addWidget(self._progress_bar)

        self.setLayout(body_layout)

    def _update_progress(self, progress: int):
        self._progress_bar.setValue(progress)

    def _update_step(self, index: int, title: str):
        self._progress_bar_label.setText(f"Step {index} of {self._installer_steps}: {title}")

    def _installer_finished(self):
        self._installer_thread.quit()
        self._finished = True

        self._progress_bar.deleteLater()
        self._progress_bar_label.setText("KeyCursor was installed successfully!")

        self._installer.setButtonLayout([QWizard.Stretch, QWizard.NextButton, QWizard.FinishButton])
