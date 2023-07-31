import os

from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursor"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor/KeyCursorApplication.py"

if __name__ == "__main__":
    step("Building executable")
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm")
