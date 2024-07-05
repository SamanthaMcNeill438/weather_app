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
    # cur.execute('CALL sp_addData(%s, %d, %d, %d, %d))', (City, Min_Temp, Max_Temp, Avg_Temp, Humiditiy))
    # cur.execute('CALL sp_searchData(%s))', (City))
    # cur.execute('CALL sp_updateData(%s, %d, %d, %d, %d))', (City, Min_Temp, Max_Temp, Avg_Temp, Humiditiy))
    # cur.execute('CALL sp_deleteData(%s))', (City))
    # cur.commit()