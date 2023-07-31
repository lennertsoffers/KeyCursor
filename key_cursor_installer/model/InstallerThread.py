from PyQt5.QtCore import QThread, pyqtSignal

from model.InstallerStep import InstallerStep
from model.InstallerStepCleanup import InstallerStepCleanup
from model.InstallerStepCopyToInstallationDirectory import InstallerStepCopyToInstallationDirectory
from model.InstallerStepDownload import InstallerStepDownload
from model.InstallerStepExtract import InstallerStepExtract
from model.InstallerStepRemovePreviousVersion import InstallerStepRemovePreviousVersion


class InstallerThread(QThread):
    _progress_signal = pyqtSignal(int)
    _step_signal = pyqtSignal(int, str)
    _finished_signal = pyqtSignal()

    def __init__(self, install_directory: str):
        super().__init__()

        self._installer_steps: list[InstallerStep] = [
            InstallerStepDownload(1, self._progress_signal),
            InstallerStepExtract(2, self._progress_signal),
            InstallerStepRemovePreviousVersion(3, self._progress_signal, install_directory),
            InstallerStepCopyToInstallationDirectory(4, self._progress_signal, install_directory),
            InstallerStepCleanup(5, self._progress_signal)
        ]

    def run(self) -> None:
        for step in self._installer_steps:
            self._execute_step(step)

        self._finished_signal.emit()

    def get_progress_signal(self) -> pyqtSignal:
        return self._progress_signal

    def get_step_signal(self) -> pyqtSignal:
        return self._step_signal

    def get_finished_signal(self) -> pyqtSignal:
        return self._finished_signal

    def get_amount_of_steps(self) -> int:
        return len(self._installer_steps)

    def _execute_step(self, installer_step: InstallerStep) -> None:
        self._step_signal.emit(installer_step.get_index(), installer_step.get_title())
        installer_step.run()
