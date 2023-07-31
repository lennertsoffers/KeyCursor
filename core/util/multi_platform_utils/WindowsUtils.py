import os.path

from util.multi_platform_utils.PlatformUtils import PlatformUtils


class WindowsUtils(PlatformUtils):
    def get_default_installation_location(self) -> str:
        return os.getenv("APPDATA").replace("\\", "/")
