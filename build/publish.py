import shutil

import paramiko

from build.build_key_cursor import build_key_cursor
from build.build_key_cursor_config import build_key_cursor_config
from build.build_key_cursor_installer import build_key_cursor_installer
from build.env_config.EnvConfig import EnvConfig
from build.util import file_utils
from build.util.file_utils import remove_file_if_exists
from build.util.log_utils import step

# --- CONFIG --- #
NAME = "KeyCursor.zip"


def publish_key_cursor():
    step("Removing old archive")
    remove_file_if_exists("./publish/KeyCursor.zip")

    build_key_cursor()
    build_key_cursor_config()
    build_key_cursor_installer()

    step("Creating archive")
    files_to_archive = [
        ("./dist/KeyCursor.exe", "KeyCursor.exe"),
        ("./dist/KeyCursorConfig.exe", "KeyCursorConfig.exe"),
        ("./resources/config.yaml", "key_cursor_config/config.yaml"),
        ("./resources/icon.png", "resources/assets/icon.png")
    ]
    file_utils.zip_files(files_to_archive, "KeyCursor.zip")

    step("Moving archive to publish directory")
    shutil.move("./KeyCursor.zip", "./publish/KeyCursor.zip")
    shutil.move("./dist/KeyCursorInstaller.exe", "./publish/KeyCursorInstaller.exe")

    step("Connecting to server")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(EnvConfig.SERVER_IP, username=EnvConfig.SERVER_USERNAME, password=EnvConfig.SERVER_PASSWORD)

    step("Uploading archive")
    sftp = ssh_client.open_sftp()
    sftp.put("./publish/KeyCursor.zip", "./key_cursor/KeyCursor.zip")
    sftp.put("./publish/KeyCursorInstaller.exe", "./key_cursor/KeyCursorInstaller.exe")
    sftp.close()
    ssh_client.close()


if __name__ == "__main__":
    publish_key_cursor()
