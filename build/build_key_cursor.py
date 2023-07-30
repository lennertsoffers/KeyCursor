import os

# --- CONFIG --- #
NAME = "KeyCursor"
ICON_PATH = "../key_cursor_config/resources/assets/icon.png"
MAIN_FILE_PATH = "../key_cursor/KeyCursor.py"

if __name__ == "__main__":
    os.system(f"pyinstaller {MAIN_FILE_PATH} --onefile --noconsole --icon=\"{ICON_PATH}\" --name {NAME} --noconfirm --clean")
