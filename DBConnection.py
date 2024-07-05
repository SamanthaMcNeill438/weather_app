import configparser
import DBConnection
import WeatherDataV1
import mainsql
import main
import sqlite3 

class DBConnection:

    dbconnection = sqlite3.connect('WeatherApp.db') 
    # my_cursor = dbconnection.cursor()

    def get_connection_string(self):
        return self.dbconnection
    
    def initialise_database(self):
        # Create a cursor object
        cursor = self.dbconnection.cursor()

        # Execute the SQL file
        with open('schema.sql', 'r') as f:
            sql_script = f.read()
            cursor.executescript(mainsql.sql)