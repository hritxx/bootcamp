import pickle

class ConfigV1:
    def __init__(self, setting):
        self.setting = setting
        self.version = 1

class ConfigV2:
    def __init__(self, setting, mode="default"):
        self.setting = setting
        self.mode = mode
        self.version = 2

    @classmethod
    def from_old(cls, old):
        return cls(old.setting)

# Simulating version upgrade
old_config = ConfigV1("light")
serialized = pickle.dumps(old_config)
loaded_old = pickle.loads(serialized)
new_config = ConfigV2.from_old(loaded_old)
print(new_config.__dict__)