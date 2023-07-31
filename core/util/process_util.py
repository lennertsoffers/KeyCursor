import psutil
from psutil import Process
from typing import List

from Global import Global


def is_key_cursor_running() -> bool:
    return len(get_key_cursor_processes()) > 0

def is_key_cursor_config_running() -> bool:
    return len(get_key_cursor_config_processes()) > 0

def get_key_cursor_processes() -> List[Process]:
    processes = []
    for process in psutil.process_iter():
        if Global.APPLICATION_NAME in process.name() and Global.APPLICATION_CONFIG_NAME not in process.name():
            processes.append(process)

    return processes

def get_key_cursor_config_processes() -> List[Process]:
    processes = []
    for process in psutil.process_iter():
        if Global.APPLICATION_CONFIG_NAME in process.name():
            processes.append(process)

    return processes
