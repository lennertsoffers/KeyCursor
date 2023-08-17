from threading import Event, Thread

from PIL import Image
from pystray import Menu, MenuItem, Icon

from Global import Global
from model.State import State
from util.process_util import start_key_cursor_config


class SystemTrayIcon:
    def __init__(self, state: State):
        self._icon = None
        self._state = state

        self._exit_event = None
        self._icon = None

    def show(self):
        self._exit_event = Event()

        tray_thread = Thread(target=self._create_icon, args=(self._exit_event,))
        tray_thread.start()

        self._exit_event.wait()

    def update(self):
        self._icon._menu = self._create_menu()
        self._icon.update_menu()

    def _on_configure_click(self, _icon, _item):
        start_key_cursor_config()

    def _on_suspend_click(self, _icon, _item):
        self._state.toggle_suspension()
        self.update()

    def _on_exit_click(self, icon, _item):
        icon.stop()
        self._exit_event.set()

    def _create_menu(self) -> Menu:
        menu_item_configure = MenuItem("Configure", self._on_configure_click, default=True)
        menu_item_suspend = MenuItem("Resume" if self._state.is_suspended() else "Suspend", self._on_suspend_click)
        menu_item_exit = MenuItem("Exit", self._on_exit_click)

        return Menu(menu_item_configure, menu_item_suspend, menu_item_exit)

    def _create_icon(self, _event):
        if not Icon.HAS_MENU or not Icon.HAS_DEFAULT_ACTION:
            return

        image = Image.open(Global.ICON_PATH)

        print("icon")

        self._icon = Icon(Global.APPLICATION_NAME, image, Global.APPLICATION_NAME, menu=self._create_menu())
        self._icon.run()
