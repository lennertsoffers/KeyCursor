import os
import shutil

# --- CONFIG --- #
NAME = "KeyCursorConfig"
ICON_PATH = "../key_cursor_config/assets/icon.png"
ASSETS_PATH = "../key_cursor_config/assets"
MAIN_FILE_PATH = "../key_cursor_config/main.py"

if __name__ == "__main__":
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm ")

    if not os.path.exists("./dist/assets"):
        shutil.copytree("../key_cursor_config/assets", "./dist/assets")
