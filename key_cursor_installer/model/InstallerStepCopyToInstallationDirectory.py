import shutil
import time

from PyQt5.QtCore import pyqtSignal

from Global import Global
from model.InstallerStep import InstallerStep


class InstallerStepCopyToInstallationDirectory(InstallerStep):
    def __init__(self, index: int, progress_signal: pyqtSignal(int), install_directory: str):
        super().__init__(index, "Copying files to installation directory", progress_signal)

        self._install_directory: str = install_directory

    def _run(self):
        try:
            shutil.copytree(Global.APPLICATION_NAME, self._install_directory)
        except shutil.Error as e:
            print(e)
        except OSError as e:
            print(e)

        time.sleep(1)
        self.get_progress_signal().emit(100)
