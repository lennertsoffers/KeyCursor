import os
import sys
import winshell
from win32com.client import Dispatch

from core.Global import Global
from autostart.AutoStart import AutoStart


def get_shortcut_folder_path():
    return os.path.join(winshell.folder("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs")


def get_shortcut_path():
    return os.path.join(get_shortcut_folder_path(), f"{Global.APPLICATION_NAME}.lnk")


def create_shortcut(target_exe, shortcut_name):
    shell = Dispatch('WScript.Shell')
    shortcut_path = os.path.join(get_shortcut_folder_path(), f"{shortcut_name}.lnk")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_exe
    shortcut.WorkingDirectory = os.path.dirname(target_exe)
    shortcut.IconLocation = target_exe
    shortcut.Save()


class AutoStartWindows(AutoStart):
    def register_autostart(self):
        if os.path.exists(get_shortcut_path()):
            return

        key_cursor_exe = os.path.join(os.path.dirname(sys.executable), f"{Global.APPLICATION_NAME}.exe")
        create_shortcut(key_cursor_exe, Global.APPLICATION_NAME)

    def disable_autostart(self):
        shortcut_path = get_shortcut_path()
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
