#gets the min, max and avg temp and humidity for a user specified city

from typing import Union
from fastapi import FastAPI, HTTPException
import json
import requests
import config
import WeatherDataV1 


app = FastAPI()
API_KEY = config.get_API_KEY()
units = config.get_units()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    
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
        #HTTPException(status_code=weather_data, detail='An error occured')
        #return {"City not found"}
        print("stopped working")
    return get_data(weather_data)
    

def get_data(weather_data):
    min_temp = weather_data["main"]["temp_min"]
    max_temp = weather_data["main"]["temp_max"]
    avg_temp = round(((min_temp + max_temp)/2),2) 
    humidity = weather_data["main"]["humidity"]
    
    # data = WeatherData(min_temp, max_temp, humidity)
    # return WeatherData.get_weather_data(data)
    return {
        "min temp:": min_temp,
        "max temp:": max_temp,
        "avg temp:": avg_temp,
        "humidity:": humidity
    }

    


