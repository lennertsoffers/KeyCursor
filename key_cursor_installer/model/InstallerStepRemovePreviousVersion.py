import os
import shutil
import time

from PyQt5.QtCore import pyqtSignal

from model.InstallerStep import InstallerStep


class InstallerStepRemovePreviousVersion(InstallerStep):
    def __init__(self, index: int, progress_signal: pyqtSignal(int), install_directory: str):
        super().__init__(index, "Removing previous version", progress_signal)

        self._install_directory: str = install_directory

    def _run(self):
        if os.path.exists(self._install_directory):
            shutil.rmtree(self._install_directory)

        time.sleep(1)
        self.get_progress_signal().emit(100)
