import os

from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursorInstaller"
ICON_PATH = "../key_cursor_installer/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor_installer/KeyCursorInstallerApplication.py"

if __name__ == "__main__":
    step("Building executable")
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm ")
