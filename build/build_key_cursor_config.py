import os

from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursorConfig"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor_config/KeyCursorConfigApplication.py"

if __name__ == "__main__":
    step("Building executable")

    start_command = (
        f"pyinstaller {MAIN_FILE_PATH} "
        f"--onefile "
        f"--noconsole "
        f"--icon=\"{ICON_PATH}\" "
        f"--name {NAME} "
        f"--noconfirm"
    )

    os.system(start_command)
