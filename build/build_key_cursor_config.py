import os

from build.util import file_utils
from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursorConfig"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor_config/KeyCursorConfigApplication.py"

RESOURCES_PATH = "../key_cursor_config/resources"
RESOURCES_OUTPUT_PATH = "./dist/resources"

if __name__ == "__main__":
    step("Building executable")
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm ")

    step("Copy resources")
    file_utils.copy_with_updates(RESOURCES_PATH, RESOURCES_OUTPUT_PATH)
