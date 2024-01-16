import json
import os


class Config:
    _data: dict = None
    @staticmethod
    def _read_config():
        try:
            file = open('config/config.json')
            Config._data = json.load(file)
        except Exception:
            raise Exception("Config file is empty.")
    @staticmethod
    def _check():
        path = 'config/config.json'
        if not os.path.exists(path):
            with open(path, "w") as file:
                d = {
                    "TG_BOT_API_KEY": ""
                }
                json_object = json.dumps(d, indent=1)
                file.write(json_object)
    @staticmethod
    def load_config():
        Config._check()
        Config._read_config()

    @staticmethod
    def get_data(*, arg):
        if Config._data is not None:
            return Config._data[arg]
        else:
            return None

