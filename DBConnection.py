import configparser
import DBConnection
import WeatherData
# import mainsql
import main
import sqlite3 

class DBConnection:

    # db_conn = DBConnection()
    my_cursor : object

    def __init__(self):
        self.dbconnection = sqlite3.connect('WeatherApp.db')
        self.my_cursor = self.dbconnection.cursor()

    def get_connection_string(self):
        return self.dbconnection
    
    def initialise_database(self):
        # Create a cursor object
        cursor = self.my_cursor
        
        try:
            # Execute the SQL file
            with open('mainsql.sql', 'r') as f:
                sql_script = f.read()
                #cursor.executescript(sql_script)
                print(sql_script)  # Print out the SQL script
                cursor.executescript(sql_script) 
        except sqlite3.OperationalError as e:
            print(f"Error executing SQL script: {e}")