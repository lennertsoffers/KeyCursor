import time
import zipfile

from PyQt5.QtCore import pyqtSignal

from model.InstallerStep import InstallerStep
from util.StepUtil import simulate_work


class InstallerStepExtract(InstallerStep):
    def __init__(self, index: int, progress_signal: pyqtSignal(int)):
        super().__init__(index, "Extracting files", progress_signal)

    def _run(self):
        with zipfile.ZipFile("key_cursor.zip", "r") as zip_ref:
            zip_ref.extractall("KeyCursor")

        simulate_work(self.get_progress_signal())
