import DBConnection
import WeatherData
import main
# import sqlite3 

class WeatherDAL:
    
    def add_weather_data(response):
        connection = DBConnection._connection_string

        # connect to database from weather
        # create add data functuion
        # create delete data function
        # create update function    
        # create searches/queries

    # DATABASE QUERIES
    # cur.execute("SELECT Min_Temp, Max_Temp, Max_Temp, Max_Temp FROM Weather WHERE City == City")
    # cur.execute(sp_addData(City, Min_Temp, Max_Temp, Avg_Temp, Humiditiy))
    # cur.commit()