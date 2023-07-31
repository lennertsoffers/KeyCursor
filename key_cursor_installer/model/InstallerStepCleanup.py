import os
import shutil

from PyQt5.QtCore import pyqtSignal

from model.InstallerStep import InstallerStep


class InstallerStepCleanup(InstallerStep):
    def __init__(self, index: int, progress_signal: pyqtSignal(int)):
        super().__init__(index, "Cleaning up temporary files", progress_signal)

    def _run(self):
        os.remove("key_cursor.zip")
        shutil.rmtree("KeyCursor")
