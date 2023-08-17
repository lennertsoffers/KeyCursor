import os

from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursorConfig"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor_config/KeyCursorConfigApplication.py"
RESOURCES_DIRECTORY_PATH = "../key_cursor_config/resources"


def build_key_cursor_config():
    step("Bundling resource files")
    bundle_command = (
        f"pyrcc5 "
        f"{RESOURCES_DIRECTORY_PATH}/resources.qrc "
        f"-o "
        f"{RESOURCES_DIRECTORY_PATH}/resources.py"
    )
    os.system(bundle_command)

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


if __name__ == "__main__":
    build_key_cursor_config()
