

class RobotDataStore():
    _data_store = {}

    @classmethod
    def set_env_var(cls, name, value):
        cls._data_store[name] = value

    @classmethod
    def get_env_var(cls, name):
        if name not in cls._data_store:
            raise KeyError(f"Key \"{name}\" does not exist in RobotDataStore")
        return cls._data_store[name]

    @classmethod
    def del_env_var(cls, name):
        if name in cls._data_store:
            del cls._data_store[name]

    @classmethod
    def del_all_vars(cls):
        cls._data_store = {}
