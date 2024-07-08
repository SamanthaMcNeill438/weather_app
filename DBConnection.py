import configparser
import DBConnection
import WeatherData
from mainsql import sql_create, sql_drop
import main
import sqlite3 

class DBConnection:

    # db_conn = DBConnection()
    my_cursor : object
    def __init__(self):
        self.connection = None
        self.my_cursor = None

    # def __init__(self):
    #     self.dbconnection = sqlite3.connect('WeatherApp.db')
    #     self.my_cursor = self.dbconnection.cursor()

    def get_connection_string(self):
        return self.connection
    
    def initialise_database(self):
        # Create a cursor object
        cursor = self.my_cursor
        
        try:
            # Execute the SQL file
            with open('mainsql.py', 'r') as f:
                self.connection = sqlite3.connect('weather_app.db')
                self.my_cursor = self.connection.cursor()  # Initialize the cursor
                self.my_cursor.execute(sql_drop)
                self.my_cursor.execute(sql_create)  # Now you can call execute on the cursor
        except sqlite3.OperationalError as e:
            print(f"Error executing SQL script: {e}")