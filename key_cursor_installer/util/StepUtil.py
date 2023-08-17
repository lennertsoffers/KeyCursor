import time

from PyQt5.QtCore import pyqtSignal


def simulate_work(progress_signal: pyqtSignal):
    for i in range(1, 11):
        time.sleep(0.05)
        progress_signal.emit(i * 100)
