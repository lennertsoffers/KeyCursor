import subprocess
import functools
from threading import Event, Thread

from PIL import Image
from pystray import Menu, MenuItem, Icon


def show_system_tray_icon():
    exit_event = Event()

    tray_thread = Thread(target=create_icon, args=(exit_event,))
    tray_thread.start()

    exit_event.wait()


def on_configure_click(_icon, _item):
    subprocess.Popen("KeyCursorConfig")


def on_exit_click(exit_event, icon, _item):
    icon.stop()
    exit_event.set()


def create_icon(exit_event):
    if not Icon.HAS_MENU or not Icon.HAS_DEFAULT_ACTION:
        return

    image = Image.open("assets/icon_old.png")

    menu_item_configure = MenuItem("Configure", on_configure_click, default=True)
    menu_item_exit = MenuItem("Exit", functools.partial(on_exit_click, exit_event))
    menu = Menu(menu_item_configure, menu_item_exit)

    icon = Icon("KeyCursor", image, "KeyCursor", menu=menu)
    icon.run()
