import configparser

class DBConnection:
    
    
    _connection_string = "mainsql.sql"

    # dbconnection = mysql.connector.connect(host = "<host-name> ", user = "<username>" , passwd = "<password>" )  
    # my_cursor = dbconnection.cursor()

    @classmethod
    def connection_string(cls):
        if cls._connection_string is None:
            config = configparser.ConfigParser()
            config.read('config.ini')  # or any other config file
            cls._connection_string = config['WEATHERAPP']['ConnectionString']
        return cls._connection_string