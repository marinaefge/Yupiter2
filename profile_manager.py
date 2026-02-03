import json

class ProfileManager:
    def __init__(self, filename='profiles.json'):
        self.filename = filename
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_profiles(self):
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file, indent=4)

    def add_profile(self, name, config):
        self.profiles[name] = config
        self.save_profiles()

    def remove_profile(self, name):
        if name in self.profiles:
            del self.profiles[name]
            self.save_profiles()

    def get_profile(self, name):
        return self.profiles.get(name, None)

    def list_profiles(self):
        return list(self.profiles.keys())
