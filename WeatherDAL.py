import DBConnection
from DBConnection import DBConnection
import WeatherData
from mainsql import sql_delete, sql_insert, sql_select, sql_update
import sqlite3 

class WeatherDAL:

    connect = DBConnection()
    connect.initialise_database()
    connection = connect.get_connection_string()
    
    #my_cursor = DBConnection.cursor()
    City : str
    Min_Temp : float
    Max_Temp : float
    Avg_Temp : float
    Humidity : float


    def __init__(self, city, min_temp, max_temp, avg_temp, humidity):
        self.City = city
        self.Min_Temp = min_temp
        self.Max_Temp = max_temp
        self.Avg_Temp = avg_temp
        self.Humidity = humidity
        self.db_connection = DBConnection()
        self.my_cursor = self.db_connection.cursor()


    
    def __init__(self, city):
        self.City = city
        self.db_connection = DBConnection()
        self.my_cursor = self.db_connection.cursor()
        

    def add_weather_data(self):
        connection = self.connection
        cur = self.my_cursor
        cur.execute(sql_insert, (self.City, self.Min_Temp, self.Max_Temp, self.Avg_Temp, self.Humidity))
        cur.commit()
        cur.close()
        connection.close()


    def search_weather_data(self):
        connection = self.connection
        cur = self.my_cursor
        cur.execute(sql_select, (self.City))
        cur.commit()
        cur.close()
        connection.close()


    def update_weather_data(self):
        connection = self.connection
        cur = self.my_cursor
        cur.execute(sql_update, (self.City, self.Min_Temp, self.Max_Temp, self.Avg_Temp, self.Humidity))
        cur.commit()
        cur.close()
        connection.close()


    def delete_weather_data(self):
        connection = self.connection
        cur = self.my_cursor
        cur.execute(sql_delete, (self.City))
        cur.commit()
        cur.close()
        connection.close()