import DBConnection
import WeatherData
import main
import mysql.connector  

class WeatherDAL:
    
    dbconnection = mysql.connector.connect(host = "<host-name> ", user = "<username>" , passwd = "<password>" )  
    my_cursor = dbconnection.cursor()

    def add_weather_data(response):
        connection = DBConnection._connection_string

        # connect to database from weather
        # create add data functuion
        # create delete data function
        # create update function    
