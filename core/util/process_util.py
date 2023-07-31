import os
import subprocess

import psutil

from Global import Global


def kill_other_key_cursor_processes() -> None:
    kill_others(get_key_cursor_processes())


def kill_other_key_cursor_config_processes() -> None:
    kill_others(get_key_cursor_config_processes())


def is_key_cursor_running() -> bool:
    return are_not_this_process(get_key_cursor_processes())


def is_key_cursor_config_running() -> bool:
    return are_not_this_process(get_key_cursor_config_processes())


def kill_others(processes) -> None:
    pid = os.getpid()

    for process in processes:
        if process.pid != pid:
            process.kill()


def are_not_this_process(processes) -> bool:
    if len(processes) > 0:
        pid = os.getpid()

        for process in processes:
            if process.pid != pid:
                return True

    return False


def get_key_cursor_processes() -> list:
    processes = []
    for process in psutil.process_iter():
        if Global.APPLICATION_NAME in process.name() and Global.APPLICATION_CONFIG_NAME not in process.name():
            processes.append(process)

    return processes


def get_key_cursor_config_processes() -> list:
    processes = []
    for process in psutil.process_iter():
        if Global.APPLICATION_CONFIG_NAME in process.name():
            processes.append(process)

    return processes


def start_key_cursor():
    subprocess.Popen("KeyCursor")


def start_key_cursor_config():
    subprocess.Popen("KeyCursorConfig")
