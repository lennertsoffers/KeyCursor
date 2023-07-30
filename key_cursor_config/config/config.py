from PyQt5.QtGui import QFont

# Font
font_poppins = QFont()
font_poppins.setFamily("Poppins")

# Images
assets_dir = "../resources/assets"
icon_path = f"{assets_dir}/icon.png"

# Stylesheets
CLASS_PROPERTY_NAME = "class"
stylesheet_folder_path = "./resources/style"
stylesheet_variables_path = "./resources/style/variables.qss"

stylesheets_KeyCursorConfig = [
    "global",
    "button",
    "checkbox",
    "label",
    "clear",
    "scroll_area",
    "key_cursor_config"
]

stylesheets_AddKeyBindDialog = [
    "global",
    "button",
    "label",
    "combobox",
    "scrollbar",
    "add_key_bind_dialog"
]
