import json

with open("./env_config/config.json") as config_file:
    config = json.load(config_file)


class EnvConfig:
    SERVER_IP = config["server_ip"]
    SERVER_USERNAME = config["server_username"]
    SERVER_PASSWORD = config["server_password"]
