import configparser

class DBConnection:
    _connection_string = None

    @classmethod
    def connection_string(cls):
        if cls._connection_string is None:
            config = configparser.ConfigParser()
            config.read('config.ini')  # or any other config file
            cls._connection_string = config['WEATHERAPP']['ConnectionString']
        return cls._connection_string