import os

from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursor"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor/KeyCursorApplication.py"


def build_key_cursor():
    step("Building executable")

    build_command = (
        f"pyinstaller {MAIN_FILE_PATH} "
        f"--onefile "
        f"--noconsole "
        f"--icon=\"{ICON_PATH}\" "
        f"--name {NAME} "
        f"--noconfirm"
    )

    os.system(build_command)
