import requests
from PyQt5.QtCore import pyqtSignal

from model.InstallerStep import InstallerStep


class InstallerStepDownload(InstallerStep):
    def __init__(self, index: int, progress_signal: pyqtSignal(int)):
        super().__init__(index, "Downloading archives", progress_signal)

    def _run(self):
        response = requests.get("https://lennertsoffers.be/hosting/key_cursor.zip", stream=True)
        total_size = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0
        with open("key_cursor.zip", "wb") as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
                bytes_downloaded += len(chunk)
                progress = int(bytes_downloaded * 100 / total_size)
                self.get_progress_signal().emit(progress)
