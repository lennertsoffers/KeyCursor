from PyQt5.QtCore import pyqtSignal


class InstallerStep:
    def __init__(self, index: int, title: str, progress_signal: pyqtSignal(int)):
        self._index: int = index
        self._title: str = title

        self._step_progress_signal: pyqtSignal = progress_signal

    def get_index(self) -> int:
        return self._index

    def get_title(self) -> str:
        return self._title

    def get_progress_signal(self) -> pyqtSignal:
        return self._step_progress_signal

    def run(self):
        self._step_progress_signal.emit(0)
        self._run()

    def _run(self):
        """Executes the step"""
        pass
