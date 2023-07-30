import os.path

import yaml

CONFIG_FILE_DIRECTORY_PATH = "./key_cursor_config"
CONFIG_FILE_PATH = "./key_cursor_config/config.yaml"


def get_config_data():
    with open(CONFIG_FILE_PATH, "r") as file:
        try:
            return yaml.load(file, Loader=yaml.FullLoader)
        except yaml.YAMLError as error:
            print(f"Error reading the config file: {error}")
            return None


def save_config_data(config_data):
    with open(CONFIG_FILE_PATH, "w") as file:
        try:
            yaml.dump(config_data, file)
            return True
        except yaml.YAMLError as error:
            print(f"Error writing to the config file: {error}")
            return False


def create_config_if_not_exists():
    if not os.path.exists(CONFIG_FILE_DIRECTORY_PATH):
        os.makedirs(CONFIG_FILE_DIRECTORY_PATH)
    if not os.path.exists(CONFIG_FILE_PATH):
        open(CONFIG_FILE_PATH, "x")


class Config:
    def __init__(self):
        create_config_if_not_exists()
        self._config_data = get_config_data()

        self._mapping = None
        self._run_at_startup = None

    def get_mapping(self):
        if self._mapping is None:
            if self._config_data and "mappings" in self._config_data:
                self._mapping = self._config_data["mappings"]
            else:
                self._mapping = {}

        return self._mapping

    def add_mapping(self, key, value):
        self._mapping[key] = value
        self._save()

    def remove_mapping(self, key):
        self._mapping.pop(key)
        self._save()

    def is_run_at_startup(self):
        if self._run_at_startup is None:
            if self._config_data and "run_at_startup" in self._config_data:
                self._run_at_startup = self._config_data["run_at_startup"]
            else:
                self._run_at_startup = False

        return self._run_at_startup

    def set_run_at_startup(self, run_at_startup):
        self._run_at_startup = run_at_startup
        self._save()

    def _save(self):
        config_data = {
            "run_at_startup": self.is_run_at_startup(),
            "mappings": self.get_mapping()
        }

        save_config_data(config_data)
