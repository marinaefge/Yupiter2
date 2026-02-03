# config_handler.py

class ConfigHandler:
    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self):
        with open(self.config_file, 'r') as file:
            config = file.readlines()
        return config

    def write_config(self, config_data):
        with open(self.config_file, 'w') as file:
            file.writelines(config_data)

    def update_config(self, key, value):
        config = self.read_config()
        # Logic to update the specific key with new value
        for i, line in enumerate(config):
            if line.startswith(key):
                config[i] = f'{key}={value}\n'
        self.write_config(config)