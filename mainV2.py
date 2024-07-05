#gets the min, max and avg temp and humidity for a user specified city
from typing import Union
from fastapi import FastAPI
import json
import requests
import config
import WeatherData


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/weather/{city}")
async def get_weather(city: str):

    data = WeatherData(city)
    response = pull_data(city)
    return data.check_if_exists(city, manage_data(response, city))



def manage_data(data, city):
    min_temp = data["main"]["temp_min"]
    max_temp = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]

    weather_data = WeatherData(city, min_temp, max_temp, humidity)
    avg_temp = weather_data.get_avg_temp()
    return {
        "min temp:": min_temp,
        "max temp:": max_temp,
        "avg temp:": avg_temp,
        "humidity:": humidity
    }


def pull_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = config.get_params(city)
    response = requests.get(base_url, params)
    weather_data = json.loads(response.text)

    if weather_data["cod"] != "200": 
        #HTTPException(status_code=weather_data, detail='An error occured')
        #return {"City not found"}
        print("stopped working")    
    return weather_data