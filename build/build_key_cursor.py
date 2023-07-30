import os

# --- CONFIG --- #
NAME = "KeyCursor"
ICON_PATH = "../key_cursor_config/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor/main.py"

if __name__ == "__main__":
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm --clean")
