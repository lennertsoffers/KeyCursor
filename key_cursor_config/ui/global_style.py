from PyQt5.QtGui import QFont

# Colours
colour_black = "#181c1f"
colour_green = "#80fe88"
colour_red = "#ff5349"
colour_white = "#f5f5f5"

# Size
spacing_small = "10px"
spacing_large = "20px"
item_height = "40px"
border_radius = "10px"

# Font
font_poppins = QFont()
font_poppins.setFamily("Poppins")
font_size_small = "10px"
font_size_normal = "13px"

# Images
assets_dir = "./assets"
image_arrow_down = f"url({assets_dir}/arrow_down.png)"
image_arrow_up = f"url({assets_dir}/arrow_up.png)"
icon_path = f"{assets_dir}/icon.png"

# Buttons
button_confirm_style = f"height: {item_height}; background-color: {colour_green}; color: {colour_black}; border-radius: {border_radius}; font-size: {font_size_normal};"
button_cancel_style = f"height: {item_height}; background-color: {colour_red}; color: {colour_black}; border-radius: {border_radius}; font-size: {font_size_normal};"

# Dropdown
dropdown_style = f"""
QComboBox {{
    border: none;
    background-color: {colour_white};
    height: {item_height};
    border-radius: {border_radius};
    padding-left: {spacing_small};
}}

QComboBox::drop-down {{
    border: 0px;
}}

QComboBox::down-arrow {{
    image: {image_arrow_down};
    width: 18px;
    height: 7px;
    padding-right: {spacing_small};
}}

QComboBox QAbstractItemView {{
    border: none;
    background: {colour_white};
    selection-background-color: {colour_green};
    selection-color: {colour_black};
    outline: 0px;
}}

QScrollBar:vertical {{
    border: none;
    background: {colour_white};
    width: 14px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}}

QScrollBar::handle:vertical {{   
    background-color: {colour_black};
    min-height: 30px;
    border-radius: 3px;
    margin: 0px 4px;
}}

QScrollBar::sub-line:vertical {{
    image: {image_arrow_up};
    border: none;
    background-color: {colour_white};
    height: 15px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}}

QScrollBar::add-line:vertical {{
    image: {image_arrow_down};
    border: none;
    background-color: {colour_white};
    height: 15px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
    background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
    background: none;
}}
"""

# Label
label_style = f"color: {colour_white}; font-size: {font_size_normal};"

# Checkbox
checkbox_style = f"color: {colour_white}; font-size: {font_size_normal}; padding-left: 5px;"
