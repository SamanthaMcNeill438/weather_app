#gets the min, max and avg temp and humidity for a user specified city

from typing import Union
from fastapi import FastAPI, HTTPException
import json
import requests 
import WeatherData
import GitignoreAccessor

ignored_files = GitignoreAccessor()
config = ignored_files.get_ignored_files()

app = FastAPI()
API_KEY = config.get_API_KEY()
units = config.get_units()
data : object


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    # """
    # Returns the weather data for a given city.

    # Args:
    #     city (str): The city for which to retrieve the weather data.

    # Returns:
    #     dict: A dictionary with keys "min temp:", "max temp:", "avg temp:", and "humidity:".

    # Raises:
    #     HTTPException: If the API request fails or the city is not found.

    # Example:
    #     >>> get_weather("London")
    #     {"min temp:": 10.0, "max temp:": 20.0, "avg temp:": 15.0, "humidity:": 60}
    # """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": units,  
        "appid": API_KEY
    }

    response = requests.get(base_url, params)
    print(response)

    weather_data = json.loads(response.text)
    print(weather_data)

    if weather_data["cod"] != "200": 
        HTTPException(status_code=weather_data, detail='An error occured')
        print("stopped working")
    return get_data(weather_data)
    
    

def get_data(weather_data):
    min_temp = weather_data["main"]["temp_min"]
    max_temp = weather_data["main"]["temp_max"]
    #avg_temp = round(((min_temp + max_temp)/2),2)
    humidity = weather_data["main"]["humidity"]
    
    data = WeatherData(min_temp, max_temp, humidity)
    return data.get_weather_data()
    # return {
    #     "min temp:": min_temp,
    #     "max temp:": max_temp,
    #     "avg temp:": avg_temp,
    #     "humidity:": humidity
    # }

    


