import configparser
import DBConnection
import WeatherData
# import mainsql
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
        
        try:
            # Execute the SQL file
            with open('mainsql.sql', 'r') as f:
                sql_script = f.read()
                #cursor.executescript(sql_script)
                print(sql_script)  # Print out the SQL script
                #cursor.executescript(sql_script)
        except sqlite3.OperationalError as e:
            print(f"Error executing SQL script: {e}")