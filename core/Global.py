import platform

from util.multi_platform_utils.LinuxUtils import LinuxUtils
from util.multi_platform_utils.MacUtils import MacUtils
from util.multi_platform_utils.WindowsUtils import WindowsUtils


class Global:
    APPLICATION_NAME = "KeyCursor"
    APPLICATION_CONFIG_NAME = "KeyCursorConfig"
    APPLICATION_INSTALLER_NAME = "KeyCursorInstaller"
    ICON_PATH = "./resources/assets/icon.png"
    CONFIG_FILE_DIRECTORY_PATH = "./key_cursor_config"
    CONFIG_FILE_PATH = "./key_cursor_config/config.yaml"

    system = platform.system()
    if system == "Windows":
        PLATFORM_UTILS = WindowsUtils()
    elif system == "Darwin":
        PLATFORM_UTILS = MacUtils()
    elif system == "Linux":
        PLATFORM_UTILS = LinuxUtils()
    else:
        raise Exception("Unsupported operating system: {}".format(system))
