import configparser
import DBConnection
import WeatherDataV1
import main
import sqlite3 

class DBConnection:

    dbconnection = sqlite3.connect('WeatherApp.db') 
    # my_cursor = dbconnection.cursor()

    def get_connection_string(self):
        return self.dbconnection